# Set the Flask app port (can be customized)
PORT = 5001

# Build the Docker container
build:
    docker build -t iss-flask-app .

# Run the Docker container
run:
    docker run -p $(PORT):5001 iss-flask-app

test:
    pytest tests/ 