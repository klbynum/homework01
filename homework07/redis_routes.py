from flask import Flask, request, jsonify
import redis
import json

app = Flask(__name__)
rd = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def home():
    return jsonify({
        "message": "use endpoint /data to load data"
    })

@app.route('/data', methods=['POST', 'GET'])
def handle_data():
    if request.method == 'POST':
        # Load data from JSON file
        with open('M7/meteorite_landings.json', 'r') as f:
            data = json.load(f)
            meteorite_landings = data['meteorite_landings']
        
        # Store each entry as a hash in Redis
        for landing in meteorite_landings:
            key = f"meteorite:{landing['id']}"
            rd.hset(key, mapping=landing)

        return jsonify({"message": "Data has been loaded into Redis", "entry count": len(meteorite_landings)})
    
    elif request.method == 'GET':
        keys = rd.keys("meteorite:*")
        all_data = []

        for key in keys: 
            redis_data = rd.hgetall(key)
            decoded = {k.decode(): v.decode() for k, v in redis_data.items()}
            all_data.append(decoded)
        
        return jsonify(all_data), 200
    
if __name__ == '__main__':
    app.run(debug=True)