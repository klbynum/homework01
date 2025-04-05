# Use Python 3.9 image from Docker Hub
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade flask werkzeug 

# Copy the application code and meteorite data file
COPY . .

# Expose the app's port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
