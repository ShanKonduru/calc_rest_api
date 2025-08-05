from flask import Flask, request, jsonify
import math
from functools import wraps
import threading



scientific_app = Flask("ScientificAPI")

# === Constant API Token ===
VALID_API_KEY = "token_string"

# === API Key Decorator ===
def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.headers.get('x-api-key')
        if not key or key != VALID_API_KEY:
            return jsonify({"error": "Unauthorized - Invalid or missing API Key"}), 401
        return f(*args, **kwargs)
    return decorated

# === Scientific Endpoints (Protected with API Key) ===
@scientific_app.route('/scientific/power', methods=['POST'])
@require_api_key
def power():
    data = request.get_json()
    base = data.get('base')
    exp = data.get('exp')
    return jsonify(result=math.pow(base, exp))

@scientific_app.route('/scientific/sqrt', methods=['POST'])
@require_api_key
def sqrt():
    data = request.get_json()
    x = data.get('x')
    if x < 0:
        return jsonify(error="Cannot compute square root of negative number"), 400
    return jsonify(result=math.sqrt(x))

@scientific_app.route('/scientific/log', methods=['POST'])
@require_api_key
def log():
    data = request.get_json()
    x = data.get('x')
    if x <= 0:
        return jsonify(error="Logarithm undefined for non-positive numbers"), 400
    return jsonify(result=math.log(x))

# === Run Scientific App on Port 5002 ===
def run_scientific():
    scientific_app.run(port=5002)

if __name__ == '__main__':
    threading.Thread(target=run_scientific).start()
