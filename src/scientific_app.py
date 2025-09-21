# In src/scientific_server.py

from flask import Flask, request, jsonify
import math
from functools import wraps

# === Constant API Token (for test environment) ===
VALID_API_KEY = "token_string"

# === Flask App ===
scientific_app = Flask("ScientificAPI")


# === API Key Decorator ===
def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.headers.get("x-api-key")
        if not key or key != VALID_API_KEY:
            return jsonify({"error": "Unauthorized - Invalid or missing API Key"}), 401
        return f(*args, **kwargs)

    return decorated


# === Helper function for request validation ===
def validate_scientific_request(keys):
    """
    Validates that the request body is a valid JSON object and contains
    all required numeric keys. Returns a tuple of (params_dict, error_response_tuple).
    """
    data = request.get_json()
    if not data or not isinstance(data, dict):
        return None, (jsonify(error="Request body must be a valid JSON object"), 400)

    params = {}
    for key in keys:
        value = data.get(key)

        if value is None:
            return None, (jsonify(error=f"Missing required parameter '{key}'"), 400)

        if not isinstance(value, (int, float)):
            return None, (jsonify(error=f"Parameter '{key}' must be a number"), 400)

        params[key] = value

    return params, None


# === Scientific Endpoints (Protected with API Key) ===
@scientific_app.route("/scientific/power", methods=["POST"])
@require_api_key
def power():
    params, error_response = validate_scientific_request(["base", "exp"])
    if error_response:
        return error_response

    return jsonify(result=math.pow(params["base"], params["exp"])), 200


@scientific_app.route("/scientific/sqrt", methods=["POST"])
@require_api_key
def sqrt():
    params, error_response = validate_scientific_request(["x"])
    if error_response:
        return error_response

    if params["x"] < 0:
        return jsonify(error="Cannot compute square root of a negative number"), 400

    return jsonify(result=math.sqrt(params["x"])), 200


@scientific_app.route("/scientific/log", methods=["POST"])
@require_api_key
def log():
    params, error_response = validate_scientific_request(["x"])
    if error_response:
        return error_response

    if params["x"] <= 0:
        return jsonify(error="Logarithm is undefined for non-positive numbers"), 400

    return jsonify(result=math.log(params["x"])), 200


# === Run Scientific App on Port 5002 ===
if __name__ == "__main__":
    scientific_app.run(port=5002, debug=True)
