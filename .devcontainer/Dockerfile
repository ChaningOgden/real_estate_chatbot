# Use an official Python runtime as the base image
FROM python:3.13

# Set the working directory in the container
WORKDIR /app

# Copy the local code to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download NLP model for Spacy
RUN python -m spacy download en_core_web_sm