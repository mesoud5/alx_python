#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
        





































































#!/usr/bin/python3

import requests
import sys

def get_todo_progress(employee_id):
    # Define API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error fetching user information")
        return
    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error fetching TODO list")
        return
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    done_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Print progress
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for todo in todos_data:
        if todo['completed']:
            print(f"\t {todo['title']}")  # Adjusted indentation

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_progress(employee_id)






























































