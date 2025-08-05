from flask import Flask, request, jsonify
import threading
import math

# === Arithmetic API ===
arithmetic_app = Flask("ArithmeticAPI")

@arithmetic_app.route('/arithmetic/add', methods=['POST'])
def add():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    return jsonify(result=a + b)

@arithmetic_app.route('/arithmetic/sub', methods=['POST'])
def subtract():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    return jsonify(result=a - b)

@arithmetic_app.route('/arithmetic/mul', methods=['POST'])
def multiply():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    return jsonify(result=a * b)

@arithmetic_app.route('/arithmetic/div', methods=['POST'])
def divide():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    if b == 0:
        return jsonify(error="Division by zero"), 400
    return jsonify(result=a / b)

# === Scientific API ===
scientific_app = Flask("ScientificAPI")

@scientific_app.route('/scientific/power', methods=['POST'])
def power():
    data = request.get_json()
    base = data.get('base')
    exp = data.get('exp')
    return jsonify(result=math.pow(base, exp))

@scientific_app.route('/scientific/sqrt', methods=['POST'])
def sqrt():
    data = request.get_json()
    x = data.get('x')
    if x < 0:
        return jsonify(error="Cannot compute square root of negative number"), 400
    return jsonify(result=math.sqrt(x))

@scientific_app.route('/scientific/log', methods=['POST'])
def log():
    data = request.get_json()
    x = data.get('x')
    if x <= 0:
        return jsonify(error="Logarithm undefined for non-positive numbers"), 400
    return jsonify(result=math.log(x))

# === Trigonometry API ===
trigonometry_app = Flask("TrigonometryAPI")

@trigonometry_app.route('/trigonometry/sin', methods=['POST'])
def sine():
    data = request.get_json()
    angle = data.get('angle')
    return jsonify(result=math.sin(math.radians(angle)))

@trigonometry_app.route('/trigonometry/cos', methods=['POST'])
def cosine():
    data = request.get_json()
    angle = data.get('angle')
    return jsonify(result=math.cos(math.radians(angle)))

@trigonometry_app.route('/trigonometry/tan', methods=['POST'])
def tangent():
    data = request.get_json()
    angle = data.get('angle')
    return jsonify(result=math.tan(math.radians(angle)))

# === Run Each App on a Separate Port ===
def run_arithmetic():
    arithmetic_app.run(port=5001)

def run_scientific():
    scientific_app.run(port=5002)

def run_trigonometry():
    trigonometry_app.run(port=5003)

if __name__ == '__main__':
    threading.Thread(target=run_arithmetic).start()
    threading.Thread(target=run_scientific).start()
    threading.Thread(target=run_trigonometry).start()
