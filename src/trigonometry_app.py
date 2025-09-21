# In src/trigonometry_app.py

from flask import Flask, request, jsonify
import math
from functools import wraps

# === User Store for Basic Auth (for test environment) ===
users = {"admin": "secret123", "user": "password"}

# === API Key (for test environment) ===
VALID_API_KEY = "token_string"

# === Flask App ===
trigonometry_app = Flask("TrigonometryAPI")


# === Combined Auth Decorator ===
def require_basic_auth_and_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Check Basic Auth
        auth = request.authorization
        if not auth or users.get(auth.username) != auth.password:
            # Return a standardized error for basic auth failure
            return (
                jsonify({"error": "Unauthorized - Invalid Basic Auth credentials"}),
                401,
                {"WWW-Authenticate": 'Basic realm="Login required"'},
            )

        # Check API Key
        api_key = request.headers.get("x-api-key")
        if api_key != VALID_API_KEY:
            # Return a standardized error for API key failure
            return jsonify({"error": "Unauthorized - Invalid or missing API Key"}), 401

        return f(*args, **kwargs)

    return decorated


# === Helper function for request validation ===
def validate_numeric_request(keys):
    """
    Validates that the request body is a valid JSON object and contains
    all required numeric keys. Returns a tuple of (params_dict, error_response_tuple).
    This function is now generic and reusable.
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


# === Trigonometric Endpoints ===
@trigonometry_app.route("/trigonometry/sin", methods=["POST"])
@require_basic_auth_and_api_key
def sine():
    params, error_response = validate_numeric_request(["angle"])
    if error_response:
        return error_response

    return jsonify(result=math.sin(math.radians(params["angle"]))), 200


@trigonometry_app.route("/trigonometry/cos", methods=["POST"])
@require_basic_auth_and_api_key
def cosine():
    params, error_response = validate_numeric_request(["angle"])
    if error_response:
        return error_response

    return jsonify(result=math.cos(math.radians(params["angle"]))), 200


@trigonometry_app.route("/trigonometry/tan", methods=["POST"])
@require_basic_auth_and_api_key
def tangent():
    params, error_response = validate_numeric_request(["angle"])
    if error_response:
        return error_response

    # Handle the case where tangent is undefined
    angle = params["angle"]
    # Use math.isclose() to handle floating-point precision issues
    if math.isclose(math.cos(math.radians(angle)), 0.0, abs_tol=1e-09):
        return jsonify(error="Tangent is undefined at 90 and 270 degrees"), 400

    return jsonify(result=math.tan(math.radians(angle))), 200


# === Run App on Port 5003 ===
if __name__ == "__main__":
    trigonometry_app.run(port=5003, debug=True)
