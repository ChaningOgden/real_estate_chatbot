# Rqurements:
    # Tensorflow - https://www.tensorflow.org/install/pip

# Use an official Python runtime as the base image
FROM python:3.12

# Dependencies
## Upgrade pip
RUN pip install --upgrade pip

## Copy the requirements file into the container
COPY requirements.txt .
COPY requirements-dev.txt .

## Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-dev.txt