import json
from flask import Flask, jsonify, request
app = Flask(__name__)
data = [{'id': 0, 'name': 'Ivan', 'languages': ['Python', 'Java']}]

@app.route('/users', methods=['GET'])
def index():
    return jsonify(data)

@app.route('/users', methods=['PUT'])
def user_upd():
    data[request.get_json()['id']] = request.get_json()
    return jsonify(data)

@app.route('/users', methods=['POST'])
def user_add():
    data.append(request.get_json())
    return jsonify(data)

@app.route('/users', methods=['DELETE'])
def uder_del():
    data.pop(request.get_json()['id'])
    pass

if __name__ == '__main__':
    app.run(debug=True)
