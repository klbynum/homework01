from flask import Flask, jsonify, request, abort
import logging
import os
import xml.etree.ElementTree as ET
import json

app = Flask(__name__)

# Initialize empty dictionaries to store the data
positional_data = {}
sighting_data = {}

# Setup logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the ISS API. Use the /load-data endpoint to load data and access various routes"
    })

@app.route('/load-data', methods=['POST', 'GET'])
def load_data():
    global positional_data, sighting_data
    try:
        positional_data.clear()
        pos_file_path = "midtermProject/ISSPositionalData.txt"

        if not os.path.exists(pos_file_path):
            logging.error(f"File not found: {pos_file_path}")
            abort(500, description="Positional data file not found.")
        try:
            with open(pos_file_path, "r") as pos_file:
                logging.info("Opening ISSPositionalData.txt")
                for line in pos_file:
                    parts = line.strip().split()
                    if len(parts) >= 4:
                        epoch = parts[0]
                        positional_data[epoch] = parts[1:]
                logging.info("Loaded positional data successfully.")

        except Exception as e:
            logging.error(f"Error reading positional data: {e}")
            abort(500, description="Error reading positional data file.")

        sighting_data.clear()
        # Check if the XML file exists
        sightFile = "midtermProject/XMLsightingData.xml"
        if not os.path.exists(sightFile):
            logging.error(f"File not found: {sightFile}")
            abort(500, description="Sighting data file not found.")

        def safe_int(value, default=0):
            try:
                return int(value)
            except ValueError:
                return default
        try:
            logging.info("Parsing XMLsightingData.xml")
            tree = ET.parse(sightFile)
            root = tree.getroot()
            for vp in root.findall("visible_pass"):
                country_name = vp.find("country").text if vp.find("country") is not None else "Unknown"
                region_name = vp.find("region").text if vp.find("region") is not None else "Unknown"
                city_name = vp.find("city").text if vp.find("city") is not None else "Unknown"

                if country_name == "Unknown" or region_name == "Unknown" or city_name == "Unknown":
                    logging.warning("Skipping entry due to missing country, region, or city.")
                    continue
                if country_name not in sighting_data:
                    sighting_data[country_name] = {}

                if region_name not in sighting_data[country_name]:
                    sighting_data[country_name][region_name] = []
                sighting_data[country_name][region_name].append({
                    "city": city_name,
                    "spacecraft": vp.find("spacecraft").text if vp.find("spacecraft") is not None else "Unknown",
                    "sighting_date": vp.find("sighting_date").text if vp.find("sighting_date") is not None else "Unknown",
                    "duration_minutes": safe_int(vp.find("duration_minutes").text) if vp.find("duration_minutes") is not None else 0,
                    "max_elevation": safe_int(vp.find("max_elevation").text) if vp.find("max_elevation") is not None else 0,
                    "enters": vp.find("enters").text if vp.find("enters") is not None else "Unknown",
                    "exits": vp.find("exits").text if vp.find("exits") is not None else "Unknown",
                    "utc_time": vp.find("utc_time").text if vp.find("utc_time") is not None else "Unknown",
                    "utc_date": vp.find("utc_date").text if vp.find("utc_date") is not None else "Unknown"
                })
            logging.info("Loaded sighting data successfully.")

        except ET.ParseError as e:
            logging.error(f"Error parsing XML file: {e}")
            abort(500, description="Invalid XML format in sighting data file.")
        except Exception as e:
            logging.error(f"Error loading sighting data: {e}")
            abort(500, description="Error loading sighting data file.")
        return jsonify({"message": "Data loaded successfully."}), 200
    except Exception as e:
        logging.error(f"Error loading data: {e}", exc_info=True)
        abort(500, description="Failed to load data.")

@app.route('/epochs', methods=['GET'])
def get_epochs():
    # Return all epochs from the positional data.
    logging.info("Epochs queried.")
    epochs = list(positional_data.keys())  # Assuming positional_data is a dictionary keyed by epoch
    return jsonify(epochs)

@app.route('/epoch/<epoch_id>', methods=['GET'])
def get_epoch_data(epoch_id):
    # Return data for a specific epoch.
    logging.info(f"Epoch {epoch_id} queried.")
    epoch = positional_data.get(epoch_id)
    if not epoch:
        abort(404, description="Epoch not found.")
    return jsonify(epoch)

@app.route('/countries', methods=['GET'])
def get_countries():
    # Return all countries from sighting data.
    logging.info("Countries queried.")
    countries = list(sighting_data.keys())  # Assuming the countries are top-level keys
    return jsonify(countries)

@app.route('/country/<country_name>', methods=['GET'])
def get_country_data(country_name: str):
    # Return information about a specific country.
    logging.info(f"Country {country_name} queried.")
    country = sighting_data.get(country_name)
    if not country:
        abort(404, description="Country not found.")
    return jsonify(country)

@app.route('/regions/<country_name>', methods=['GET'])
def get_regions_by_country(country_name: str):
    # Return all regions for a specific country.
    logging.info(f"Regions for country {country_name} queried.")
    country_data = sighting_data.get(country_name)
    if not country_data:
        abort(404, description="Country not found.")
    return jsonify(list(country_data.keys()))  # Regions are keys under each country

@app.route('/region/<country_name>/<region_name>', methods=['GET'])
def get_region_data(country_name: str, region_name: str):
    # Return data on a specific region
    logging.info(f"Region {region_name} for country {country_name} queried.")
    country_data = sighting_data.get(country_name)
    if not country_data:
        abort(404, description="Country not found.")
    region = country_data.get(region_name)
    if not region:
        abort(404, description="Region not found.")
    return jsonify(region)

@app.route('/cities/<country_name>/<region_name>', methods=['GET'])
def get_cities_by_region(country_name: str, region_name: str):
    # Return all cities for a specific country and region.
    logging.info(f"Cities in region {region_name} of country {country_name} queried.")
    country_data = sighting_data.get(country_name)
    if not country_data:
        abort(404, description="Country not found.")

    region = country_data.get(region_name)
    if not region:
        abort(404, description="Region not found.")
    cities = [entry["city"] for entry in region]
    return jsonify(cities)

@app.route('/city/<country_name>/<region_name>/<city_name>', methods=['GET'])
def get_city_data(country_name: str, region_name: str, city_name: str):
    # Return data for a specific city.
    logging.info(f"City {city_name} in region {region_name} of country {country_name} queried.")
    country_data = sighting_data.get(country_name)
    if not country_data:
        abort(404, description="Country not found.")

    region = country_data.get(region_name)
    if not region:
        abort(404, description="Region not found.")

    city_data = next((entry for entry in region if entry["city"] == city_name), None)
    if not city_data:
        abort(404, description="City not found.")
    return jsonify(city_data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change port as needed
