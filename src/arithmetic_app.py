from flask import Flask, request, jsonify
from functools import wraps

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

# === Helper function for request validation ===
def validate_arithmetic_request():
    data = request.get_json()
    
    # Check if a valid JSON object was sent
    if not isinstance(data, dict):
        return None, None, jsonify(error="Request body must be a valid JSON object"), 400
    
    a = data.get('a')
    b = data.get('b')
    
    # Check for required parameters
    if a is None or b is None:
        return None, None, jsonify(error="Both 'a' and 'b' must be present"), 400

    # Check for correct data types
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None, None, jsonify(error="Both 'a' and 'b' must be numbers"), 400

    # Return the numbers and no error
    return a, b, None, None

# === Arithmetic Endpoints with Basic Auth ===
@arithmetic_app.route('/arithmetic/add', methods=['POST'])
@require_basic_auth
def add():
    a, b, error_response, status_code = validate_arithmetic_request()
    if error_response:
        return error_response, status_code
    return jsonify(result=a + b)

@arithmetic_app.route('/arithmetic/sub', methods=['POST'])
@require_basic_auth
def subtract():
    a, b, error_response, status_code = validate_arithmetic_request()
    if error_response:
        return error_response, status_code
    return jsonify(result=a - b)

@arithmetic_app.route('/arithmetic/mul', methods=['POST'])
@require_basic_auth
def multiply():
    a, b, error_response, status_code = validate_arithmetic_request()
    if error_response:
        return error_response, status_code
    return jsonify(result=a * b)

@arithmetic_app.route('/arithmetic/div', methods=['POST'])
@require_basic_auth
def divide():
    a, b, error_response, status_code = validate_arithmetic_request()
    if error_response:
        return error_response, status_code
    
    if b == 0:
        return jsonify(error="Division by zero"), 400
        
    return jsonify(result=a / b)

# === Run App on Port 5001 ===
if __name__ == '__main__':
    arithmetic_app.run(port=5001)