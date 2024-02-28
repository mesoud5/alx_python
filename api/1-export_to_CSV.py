#!/usr/bin/python3

import csv
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

    # Write data to CSV
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos_data:
            csv_writer.writerow([employee_id, employee_name, todo['completed'], todo['title']])

    print(f"Data exported to {filename}")


