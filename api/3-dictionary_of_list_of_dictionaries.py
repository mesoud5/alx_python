#!/usr/bin/python3
"""
This script retrieves all tasks from all employees and exports the data in JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    # API endpoint
    url = "https://jsonplaceholder.typicode.com/todos"

    # Send GET request
    response = requests.get(url)
    todos = response.json()

    # Dictionary to store tasks grouped by user ID
    tasks_by_user = {}

    # Group tasks by user ID
    for todo in todos:
        user_id = todo.get("userId")
        task_info = {"username": todo.get("username"), "task": todo.get("title"), "completed": todo.get("completed")}
        
        if user_id in tasks_by_user:
            tasks_by_user[user_id].append(task_info)
        else:
            tasks_by_user[user_id] = [task_info]

    # Export tasks data to JSON files
    for user_id, tasks in tasks_by_user.items():
        filename = f"{user_id}.json"
        with open(filename, "w") as f:
            json.dump(tasks, f, indent=4)

    # Export all tasks data to a single JSON file
    with open("todo_all_employees.json", "w") as f:
        json.dump(tasks_by_user, f, indent=4)
