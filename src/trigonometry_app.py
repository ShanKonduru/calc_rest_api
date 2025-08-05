from flask import Flask, request, jsonify
import math
from functools import wraps
import threading


trigonometry_app = Flask("TrigonometryAPI")

# === User Store for Basic Auth ===
users = {
    "admin": "secret123",
    "user": "password"
}

# === API Key ===
VALID_API_KEY = "token_string"

# === Combined Auth Decorator ===
def require_basic_auth_and_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Check Basic Auth
        auth = request.authorization
        if not auth or users.get(auth.username) != auth.password:
            return jsonify({"error": "Invalid Basic Auth credentials"}), 401, {'WWW-Authenticate': 'Basic realm="Login required"'}

        # Check API Key
        api_key = request.headers.get("x-api-key")
        if api_key != VALID_API_KEY:
            return jsonify({"error": "Invalid or missing API Key"}), 401

        return f(*args, **kwargs)
    return decorated

# === Trigonometric Endpoints ===
@trigonometry_app.route('/trigonometry/sin', methods=['POST'])
@require_basic_auth_and_api_key
def sine():
    data = request.get_json()
    angle = data.get('angle')
    return jsonify(result=math.sin(math.radians(angle)))

@trigonometry_app.route('/trigonometry/cos', methods=['POST'])
@require_basic_auth_and_api_key
def cosine():
    data = request.get_json()
    angle = data.get('angle')
    return jsonify(result=math.cos(math.radians(angle)))

@trigonometry_app.route('/trigonometry/tan', methods=['POST'])
@require_basic_auth_and_api_key
def tangent():
    data = request.get_json()
    angle = data.get('angle')
    return jsonify(result=math.tan(math.radians(angle)))

# === Run App on Port 5003 ===
def run_trigonometry():
    trigonometry_app.run(port=5003)

if __name__ == '__main__':
    threading.Thread(target=run_trigonometry).start()
