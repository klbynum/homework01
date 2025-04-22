# Flask Redis Meteorite Landings App
This is a containerized Flask application that interacts with a Redis database.

- - **POST** request: Loads Meteorite Landings data from a `meteoriteSites2.json` file into the Redis database.
- - **GET** request: Retrieves the Meteorite Landings data from Redis and returns it as a JSON response.
 
The Meteorite Landings data is stored in a `meteoriteSites2.json` file and is loaded into Redis on a POST request.
 
## Prerequisites
- Docker
- Docker compose

## Setup and Running the App
### 1. Fork this repository

### 2. Clone this repository

### 3. Build and Run the Application
```docker-compose up --build```

### 4. Access the Flask App
```http://localhost:5000```

### 5. Test the Application
Load Data into Redis (POST Request):
```curl -X POST http://localhost:5000/data``` <br>
Retrieve Data from Redis (GET Request): 
```curl -X GET http://localhost:5000/data```
