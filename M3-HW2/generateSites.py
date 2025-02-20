import random
import json

# Function to generate random landing sites
def generateSites():
    sites = []
    compositions = ["stony", "iron", "stony-iron"]

    for siteID in range (1,6):
        latitude = round(random.uniform(16.0, 18.0), 6)
        longitude = round(random.uniform(82.0, 84.0), 6)
        composition = random.choice(compositions)

        site = {
            "siteID": siteID,
            "latitude": latitude,
            "longitude": longitude,
            "composition": composition
        }
        sites.append(site) # add site to list of sites

    return {"sites": sites}

# Save the data to the JSON file
def saveData(data, filename="meteoriteSites.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Generate landing sites and save it
if __name__ == "__main__":
    landingSitesData = generateSites()
    saveData(landingSitesData)
    print("\n",landingSitesData,"\n")
    print("Meteorite landing sites generated and saved to the .json file")
