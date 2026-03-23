import sys
import os
sys.path.append(os.path.dirname(__file__))

from flask import Flask, request, jsonify
from tasks import add_task, get_tasks, delete_task

app = Flask(__name__)

@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(get_tasks())

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    task = add_task(data["task"])
    return jsonify({"task": task}), 201

@app.route("/tasks/<task_name>", methods=["DELETE"])
def remove_task(task_name):
    if delete_task(task_name):
        return jsonify({"message": f"Task '{task_name}' deleted successfully"}), 200
    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)