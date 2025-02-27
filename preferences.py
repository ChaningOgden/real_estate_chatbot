import json

def save_preferences(new_data):
    try:
        with open("user_preferences.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open("user_preferences.json", "w") as file:
        json.dump(data, file, indent=4)

def load_preferences():
    try:
        with open("user_preferences.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}