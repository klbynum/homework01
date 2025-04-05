import redis
from flask import Flask, request, jsonify
import json
from typing import Dict, Any
import os

# Initialize Flask app
app = Flask(__name__)

# Connect to Redis
redis_client = redis.StrictRedis(
    host=os.getenv('REDIS_HOST', 'localhost'), 
    port=6379, 
    db=0, 
    decode_responses=True
)
# File path to the meteorite data JSON
METEORITE_DATA_FILE = '/homework01/M6-HW5/meteoriteSites2.json'


def load_meteorite_data() -> list:
    if os.path.exists(METEORITE_DATA_FILE):
        with open(METEORITE_DATA_FILE, 'r') as file:
            return json.load(file)
    else:
        raise FileNotFoundError(f"The file {METEORITE_DATA_FILE} does not exist.")


@app.route('/data', methods=['POST', 'GET'])
def handle_data() -> Dict[str, Any]:
    if request.method == 'POST':
        try:
            # Load the data from the JSON file
            meteorite_data = load_meteorite_data()
            # Store data in Redis
            redis_client.set('meteorite_data', json.dumps(meteorite_data))
            return jsonify({"message": "Data loaded successfully into Redis."}), 200
        except FileNotFoundError as e:
            return jsonify({"error": str(e)}), 404
        except redis.exceptions.RedisError as e:
            return jsonify({"error": f"Error storing data in Redis: {e}"}), 500
    elif request.method == 'GET':
        try:
            # Retrieve data from Redis
            data = redis_client.get('meteorite_data')
            if data is None:
                return jsonify({"error": "No data found in Redis."}), 404
            return jsonify(json.loads(data)), 200
        except redis.exceptions.RedisError as e:
            return jsonify({"error": f"Error retrieving data from Redis: {e}"}), 500


if __name__ == '__main__':
    # Run Flask app
    app.run(host='0.0.0.0', port=5000)
