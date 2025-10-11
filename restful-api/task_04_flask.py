from flask import Flask
from flask import jsonify
from flask import request

# create application
app = Flask(__name__)

users = {}


# task 1: define the endpoint
@app.route("/")
def home():
    return "<p>Welcome to the Flask API!</p>"


# task 2: return json res
@app.route("/data")
def get_names():
    return jsonify(list(users.keys()))


# task 3: return status
@app.route("/status")
def status():
    return "OK"


# task 4: return the user object
@app.route("/users/<username>")
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    user = users[username]
    user["username"] = username

    return jsonify(user)


# task 5: add a new user
@app.route("/add_user", methods=['POST'])
def add_user():
    # parse the incoming JSON data
    data = request.get_json()

    if not data:
        return jsonify({"error": "no input data received"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Add user to dict
    users[username] = {
        "username": data.get("username"),
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
