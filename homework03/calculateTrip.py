import json
import math

# Haversine formula to calculate great-circle
def haversine(lat1, lon1, lat2, lon2):
    R = 3389.5 # Radius of Mars in km
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1,lon1,lat2,lon2]) # convert to radians
    dlat = lat2-lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

# Calculate the time to travel and sample each site
def calculateTripTime(filename="meteoriteSites.json"):
    # Read the JSON data from the file
    with open(filename, "r") as file:
        data = json.load(file)
    
    # Initial starting coordinates
    startLatitude = 16.0
    startLongitude = 82.0

    totalTime = 0
    previousLat, previousLon = startLatitude, startLongitude

    # For each site, calculate travel time and sampling time
    for leg, site in enumerate(data["sites"], 1):
        lat, lon = site["latitude"], site["longitude"]
        composition = site["composition"]

        # Calculate travel time
        distance = haversine(previousLat,previousLon,lat,lon)
        travelTime = distance / 10 # Robot's max speed is 10 km/h

        # Determine the sampling time based on composition
        if composition == "stony":
            sampleTime = 1
        elif composition == "iron":
            sampleTime = 2
        elif composition == "stony-iron":
            sampleTime = 3

        # total time for the leg (travel + sample)
        totalTime += travelTime + sampleTime

        # Print leg details
        print(f"leg = {leg}, time to travel = {travelTime:.2f} hr, time to sample = {sampleTime} hr")

        # Update the previous coordinates
        previousLat, previousLon = lat, lon

    # Print total time and number of legs
    print("==================")
    print(f"number of legs = 5, total time = {totalTime:.2f} hr")

# Run the trip calculation

if __name__ == "__main__":
    calculateTripTime()