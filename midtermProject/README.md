# ISS Tacker API 
A Flask-based, Dockerized web API that allows users to query International Space
Station (ISS) positional and sighting data using structured, user-friendly endpoints.
Built to simplify exploration of ISS tracking data and sightings over global locations.

--- 

## Project Description
This API loads and processes two ISS-related datasets: 
- **Positional Data**: Timestamped position/velocity vectors of the ISS.
- **Sighting Data**: Visibility events of the ISS over cities in the United States.
Users can interact with the API to retrieve data by **epoch**, **country**, **region**,
and **city**. The application is fully containerized with Docker for ease of deployment
and includes units tests using `pytest`.

---
## Installation & Running Locally

### 1. Clone the Repository
```bash
git clone
cd iss-tracker-api
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the Flask App
```bash
python app/main.py
```
### 4. Load Data into Memory
```bash
curl -X POST http://localhost:5001/load-data
```

## API Usage Examples
### Load Data 
```bash
POST /load-data
Response: {"message": "Data loaded successfully"}
```

### Get All Epochs
```bash
GET /epochs
Response: ["2022-02-11T12:00:00.000", "2022-02-11T12:04:00.000", ...]
```

### Get Data for a Specfic Epoch
```bash
GET /epoch/2022-02-26T12:00:00.000
Response: {
"6626.502728847900",
  "-824.239283578077",
  "-1255.363342665360",
  "-0.48760287876275",
  "4.93125830602422",
  "-5.84543261302229"
}
```
### Get All Countries
```bash
GET /countries
Response: ["United_Sates"]
```
### Drill Down by Country/Region/City
- /countries/<country_name>
- /regions/<country_name>
- /region/<country_name>/<region_name>
- /cities/<country_name>/<region_name>
- /city/<country_name>/<region_name>/<city_name>

## Running with Docker
### 1. Build the Docker Image
```bash
make build
```
### 2. Run the Container
```bash
make run
```
### 3. Run Tests Inside the Container
```bash
make test
```
### Docker Hub Image
```bash
docker pull klbynum/iss-flask-app:latest
docker run -p 5001:5001 klbynum/iss-flask-app
```

## How to Contribute
1. Fork the repository.
2. Create a new branch (```git checkout -b feature/your-feature```).
3. Commit your changes (```git commit -am 'Add some feature'```).
4. Push to the branch (```git push origin feature/your-feature```).
5. Open a Pull Request.

## Notes on Interpreting Results
- Epoch values are timestamps from the positional data, each maps to a full state vector
- Sightings are hierarchical: countries -> regions -> cities -> visibility details.
- Data must be loaded using ```/load-data ```
