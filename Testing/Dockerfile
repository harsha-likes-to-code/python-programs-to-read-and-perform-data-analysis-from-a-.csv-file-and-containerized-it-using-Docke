# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY Testing/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the test code
COPY Testing/test_orders_analysis.py /app/

# Copy the application code
COPY app /app/app

# Install pytest for testing
RUN pip install pytest

# Set PYTHONPATH to include the app directory
ENV PYTHONPATH=/app

# Command to run the tests
CMD ["pytest", "test_orders_analysis.py"]


