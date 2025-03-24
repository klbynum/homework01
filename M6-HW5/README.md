# Flask Redis Meteorite Landings App
This is a containerized Flask application that interacts with a Redis database.

- - **POST** request: Loads Meteorite Landings data from a `meteoriteSites.json` file into the Redis database.
- - **GET** request: Retrieves the Meteorite Landings data from Redis and returns it as a JSON response.
 
The Meteorite Landings data is stored in a `meteoriteSites.json` file and is loaded into Redis on a POST request.
 
## Prerequisites
- Docker
- Docker compose

## Setup and Running the App
### 1. Clone this repository
```hh
```
### 2. Build and Run the Application
```docker-compose up --build```
### 3. Access the Flask App
```http://localhost:5000```
### 4. Test the Application
Load Data into Redis (POST Request)
```curl -X POST http://127.0.0.1:5000/data```
Retrieve Data from Redis (GET Request)
```curl http://127.0.0.1:5000/data
