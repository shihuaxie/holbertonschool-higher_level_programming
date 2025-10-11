#!/usr/bin/python3

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)

# Configuration
app.config["JWT_SECRET_KEY"] = "super-secret-key"

# Instance of moudle
auth = HTTPBasicAuth()
jwt = JWTManager(app)


# users in "database"
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
        },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
        }
}


# basic AUTH
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return None
    if check_password_hash(user["password"], password):
        return username    # return 'authorizedf user'


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# JWT Authentication
@app.route("/login", methods=["POST"])
def login():
    """
    Receive JSON: {"username": "...", "password": "..."}
    Authenticate and return {"access_token": "<JWT>"}，fail with 401
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Put username/role to identity, can access it by get_jwt_identity()
    token = create_access_token(
        identity={"username": username, "role": user["role"]}
        )
    return jsonify({"access_tokrn": token})


@app.route("/jwt-protected")
@jwt_required()
def jwy_protected():
    return "JWT Auth: Access Granted"


# Role-based Protected Route
@app.route("/admin-only")
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    if not identity or identity.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# JWT error msg
@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh(err):
    return jsonify({"error": "Fresh token required"}), 401


# RUN
if __name__ == "__main__":
    app.run()
