import json
import sys
import logging
import math
from typing import List, Tuple
from collections import Counter

# CONST
turbidityThreshold = 1.0 # NTU
decayFactor = 0.02 # 2% per hour
QUADRANTS = {
    "NE": "Northern & Eastern",
    "NW": "Northern & Western",
    "SE": "Southern & Eastern",
    "SW": "Southern & Western"
}
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
def calculateTurbidity(calibrationCONST: List[float], detector_currents: List[float]) -> float:
    """Calculate turbidity using the formula T = a0*I90"""
    turbidityValues = [a0*I90 for a0, I90 in zip(calibrationCONST, detector_currents)]
    return sum(turbidityValues)/len(turbidityValues)

def calculateTimetoSafeTurbidity(currentTurbidity: float) -> float:
    if currentTurbidity <= turbidityThreshold:
        return 0.0
    b = math.log(turbidityThreshold/currentTurbidity)/math.log(1-decayFactor)
    return round(b,2)

def check_hemisphere(latitude: float, longitude: float) -> str:
    if latitude >= 0:
        if longitude >= 0:
            return "NE"
        else:
            return "NW"
    
    else: 
        if longitude >= 0:
            return "SE"
        else:
            return "SW"




def main():
    """Main function to read meteorite data and perform required calculations."""
    if len(sys.argv) != 2:
        print(f"Error: Expected 1 argument, but got {len(sys.argv) - 1}.\n")
        print("Usage: python turbidityAnalysis.py M4-HW3/turbidity_data.json")
        print("Command-line arguments:", sys.argv)
        sys.exit(1)
    
    json_file = sys.argv[1]

    # Load JSON data
    try:
        with open('M5-HW4/meteoriteSites2.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File {'M5-HW4/meteoriteSites2.json'} not found.")
        sys.exit(1)

    # get meteorite site data
    meteoriteData = data.get('sites', [])

    # Summarize hemisphere data
    hemisphere_count = Counter()
    composition_count = Counter()
    total_mass = 0
    numMeteors = len(meteoriteData)

    # loop over each meteorite site
    for site in meteoriteData:
        hemisphere = check_hemisphere(site['latitude'], site['longitude'])
        hemisphere_count[hemisphere] += 1

        # composition count 
        composition_count[site['composition']] += 1

        # average mass 
        mass = site.get('mass', 0) # Default mass
        total_mass += site.get('mass', 0)

    # Print out the summary information
    print("\nSummary data following meteorite analysis:\n")

    # Average Mass Calculation
    average_mass = total_mass/ numMeteors if numMeteors > 0 else 0
    print(f"Average mass of {numMeteors} meteor(s): {average_mass:.1f} grams\n")

    # Hemisphere summary data
    print("Hemisphere summary data:")
    for quadrant, count in hemisphere_count.items():
        print(f"There were {count} meteors found in the {QUADRANTS[quadrant]} quadrant")
    
    # Class summary data
    print("\nClass summary data:")
    for composition, count in composition_count.items():
        print(f"The {composition} class was found {count} times")

if __name__ == "__main__":
    main()