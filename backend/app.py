from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Store tasks as a list of dicts
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    tasks.append({"name": data['task']})
    return jsonify({"status": "success"}), 201

@app.route('/tasks', methods=['DELETE'])
def delete_task():
    data = request.get_json()
    task_name = data.get('task')
    global tasks
    tasks = [t for t in tasks if t['name'] != task_name]
    return jsonify({"status": "deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
