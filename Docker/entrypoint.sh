#!/bin/bash
set -e

# Train the model before starting the chatbot
python ml_model.py

# Start the chatbot
exec python app.py