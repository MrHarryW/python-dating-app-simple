import json

def load_data():
    with open("user_data.json", "r") as f:
        return json.load(f)

def save_data(data):
    with open("user_data.json", "w") as f:
        json.dump(data, f, indent=4)

def save_user(profile):
    data = load_data()
    data["users"].append(profile)
    save_data(data)
