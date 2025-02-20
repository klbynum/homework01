import json
import logging
import math
from typing import List, Tuple

# CONST
turbidityThreshold = 1.0 # NTU
decayFactor = 0.02 # 2% per hour

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

def main():
    """Main function to read turbidity data and perform required calculations."""
    # Load JSON data
    with open('M4-HW3/turbidity_data.json', 'r') as file:
        data = json.load(file)

    # Get most recent five data points
    lastestData = data['turbidity_data'][-5:]

    calibrationCONST = [entry['calibration_constant'] for entry in lastestData]
    detector_currents = [entry['detector_current'] for entry in lastestData]

    # Calculate current turbidity
    currentTurbidity = calculateTurbidity(calibrationCONST, detector_currents) 
    print(f'Average turbidity based on most recent five measurements = {currentTurbidity: .4f} NTU')

    # Check if turbidity is safe and log the appropriate message
    if currentTurbidity > turbidityThreshold:
        logging.warning('Turbidity is above thershold for safe use')
    else:
        logging.info('Turbidity is below threshold for safe use')

    # Calculate time to reach safe turbidity
    timeToSafe = calculateTimetoSafeTurbidity(currentTurbidity)
    print(f'Minimum time required to return below a safe threshold = {timeToSafe} hours')


if __name__ == "__main__":
    main()