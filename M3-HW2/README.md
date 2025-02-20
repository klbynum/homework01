# Mars Meteorite Exploration

This project simulates the journey of a robotic vehicle on Mars to visit five
meteorite landing sites in Syrtis Major. The robot generates random meteorite 
site data, calculates the time required to travel between these sites, and takes
samples based on the meteorite composition.

## Files in this reposittory
- `generateSites.py`: A Python script to randomly generate meteorite landing sites on Mars.
- `calculateTrip.py`: A Python script that reads the meteorite site data and calculates the
travel and sampling times. 
- `meteoriteSites.json`: A JSON file containing the generated meteorite landing sites data.

# Instructions to Run the code

1. Run `generateSites.py` to generate a random set of meteorite landing sites:
```bash 
python generateSites.py
