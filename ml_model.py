import numpy as np
import json
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense

# Load preferences
def load_training_data():
    try:
        with open("user_preferences.json", "r") as file:
            data = json.load(file)
            X = []
            y = []
            for key, value in data.items():
                if "liked" in key:
                    X.append([value["price"], value["acres"]])
                    y.append(1)  # Liked
                elif "disliked" in key:
                    X.append([value["price"], value["acres"]])
                    y.append(0)  # Disliked
            return np.array(X), np.array(y)
    except FileNotFoundError:
        return np.array([]), np.array([])

# Train a Neural Network
def train_neural_network():
    X, y = load_training_data()
    
    if X.shape[0] == 0:
        return None

    model = keras.Sequential([
        Dense(10, activation="relu", input_shape=(2,)),
        Dense(5, activation="relu"),
        Dense(1, activation="sigmoid")
    ])

    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    model.fit(X, y, epochs=50, verbose=0)
    
    model.save("model.h5")
    return model

# Predict next properties
def predict_next_properties(model, user_prefs):
    if not model:
        return []

    # Mock new properties (real data should come from `scraper.py`)
    new_properties = [
        {"address": "123 Lake Rd", "price": 550000, "acres": 15},
        {"address": "456 Forest Dr", "price": 580000, "acres": 12},
        {"address": "789 Mountain Ln", "price": 595000, "acres": 11},
    ]
    
    X_new = np.array([[prop["price"], prop["acres"]] for prop in new_properties])
    predictions = model.predict(X_new)

    # Return top matches
    sorted_props = sorted(zip(predictions.flatten(), new_properties), reverse=True)
    return [prop[1] for prop in sorted_props[:3]]