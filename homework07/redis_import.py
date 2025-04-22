import redis
import json

# Read meteorite_landings.json file
with open('homework07/meteorite_landings.json', 'r') as f:
    data = json.load(f)
    meteorite_landings = data['meteorite_landings']

# Connect to Redis
rd = redis.Redis(host='localhost', port=6379, db=0)

# Store each meteorite entry as a Redis hash
for landing in meteorite_landings:
    key = f"meteorite:{landing['id']}"
    rd.hset(key, mapping=landing)

print("--------Exercise 2--------\n")
print("Check the total number of keys in your Redis database against the total number of objects in "
"the JSON file.\n")
print("Read all of the landing objects out of Redis and check that each object has the correct fields.\n")

# Check total number of keys
keys = rd.keys("meteorite:*")
print(f"Total meteorite entries in Redis: {len(keys)}")
print(f"Expected entries from file: {len(meteorite_landings)}")
assert len(keys) == len(meteorite_landings), "Mismatch in number of stored keys."

# Check that each hash has the correct data 
for landing in meteorite_landings:
    key = f"meteorite:{landing['id']}"
    redis_data = rd.hgetall(key)

    # Convert Redis bytes to strings
    bytes_to_string = {k.decode(): v.decode() for k, v in redis_data.items()}

    # Convert values in original .json file to strings for effective comparison
    original_to_strings = {k: str(v) for k, v in landing.items()}

    assert bytes_to_string == original_to_strings, f"Data mismatch for {key}"

print("All data stored and verfied!")

