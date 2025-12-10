import json

def load_data():
    with open("user_data.json", "r") as f:
        return json.load(f)

def save_data(data):
    with open("user_data.json", "w") as f:
        json.dump(data, f, indent=4)

def username_exists(username):
    data = load_data()
    for user in data["users"]:
        if user["username"] == username:
            return True
    return False

def validate_login(username, password):
    data = load_data()
    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            return user  # Return the entire saved user object
    return None

def save_user(username, password, profile):
    data = load_data()
    data["users"].append({
        "username": username,
        "password": password,
        "profile": profile
    })
    save_data(data)
