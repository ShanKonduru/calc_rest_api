from flask import Flask, request, jsonify
import threading
import math
from functools import wraps
import base64

# === User store ===
users = {
    "admin": "secret123",
    "user": "password"
}

# === Flask App ===
arithmetic_app = Flask("ArithmeticAPI")

# === Basic Auth Decorator ===
def require_basic_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or users.get(auth.username) != auth.password:
            return jsonify({"error": "Unauthorized"}), 401, {'WWW-Authenticate': 'Basic realm="Login required"'}
        return f(*args, **kwargs)
    return decorated

# === Arithmetic Endpoints with Basic Auth ===
@arithmetic_app.route('/arithmetic/add', methods=['POST'])
@require_basic_auth
def add():
    data = request.get_json()
    return jsonify(result=data['a'] + data['b'])

@arithmetic_app.route('/arithmetic/sub', methods=['POST'])
@require_basic_auth
def subtract():
    data = request.get_json()
    return jsonify(result=data['a'] - data['b'])

@arithmetic_app.route('/arithmetic/mul', methods=['POST'])
@require_basic_auth
def multiply():
    data = request.get_json()
    return jsonify(result=data['a'] * data['b'])

@arithmetic_app.route('/arithmetic/div', methods=['POST'])
@require_basic_auth
def divide():
    data = request.get_json()
    if data['b'] == 0:
        return jsonify(error="Division by zero"), 400
    return jsonify(result=data['a'] / data['b'])

# === Run App on Port 5001 ===
def run_arithmetic():
    arithmetic_app.run(port=5001)

if __name__ == '__main__':
    threading.Thread(target=run_arithmetic).start()
