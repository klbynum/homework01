# Turbidity Analysis & Meteorite Classification
## 📚 Project Overview
<br>This project provides tools to analyze meteorite landing data and calculate turbidity levels, alongside tests for verifying the correctness of the analysis. The main functionalities include:

- Calculating turbidity based on provided calibration constants and detector current values.

- Estimating time until turbidity reaches a safe threshold.

- Classifying meteorite sites by hemisphere and composition.

- Running tests using pytest to ensure the reliability of all functions.

- The code is containerized using Docker for easy deployment and testing.

## 📁 Files Overview
`turbidityAnalysis2.py` — Main script to perform meteorite data analysis and turbidity calculations.

`test_turbidityAnalysis2.py` — Test suite using pytest to validate all core functions.

Dockerfile — Defines a Docker image with Python, dependencies, and the necessary setup to run the analysis and tests.

`meteoriteSites2.json` — Sample meteorite data for testing, structured as a JSON array.

📥 Expected Input Data
The meteorite site data should follow this format:

```{ 
    "sites": [
        {
            "siteID": 1,
            "latitude": 17.482853,
            "longitude": 83.114404,
            "mass": 8065,
            "composition": "stony"
        },
        {
            "siteID": 2,
            "latitude": 17.112462,
            "longitude": 83.15504,
            "mass": 1500,
            "composition": "iron"
        }
    ]
}
```

To test with additional data, download the extended meteorite dataset from this link: Meteorite Landing Data

## 🚢 Using the Docker Image
### 📦 Pull the pre-built Docker image from Docker Hub
```
docker pull klbynum466/turbidityanalysis2:homework02
```
### 🏗️ Build the Docker image locally
If you prefer to build from the Dockerfile, use the following command:

```
docker build -t klbynum466/turbidityanalysis2:homework02 .
```
▶️ Run the containerized code against the sample data
To run the meteorite analysis with the sample data included in the container:

```
docker run klbynum466/turbidityanalysis2:homework02 python turbidityAnalysis2.py M5-HW4/meteoriteSites2.json
```
### 📤 Run with user-provided data
If you have your own dataset, first download the file locally, then mount the volume when running the container:

```
docker run -v $(pwd):/app klbynum466/turbidityanalysis2:homework02 python turbidityAnalysis2.py /app/ML_Data_Sample.json
```
This command:

- sets the current directory into the container's /app folder.

- Runs the analysis using the provided `ML_Data_Sample.json`.

### 🧪 Run tests with pytest
To execute the test suite inside the container:

```
docker run klbynum466/turbidityanalysis2:homework02 pytest test_turbidityAnalysis2.py
```
Expected output will confirm whether tests pass or fail, with detailed error logs if any test fails.
