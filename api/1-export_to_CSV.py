#!/usr/bin/python3

import requests
import sys
import csv

def export_to_csv(employee_id):
    # Define API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error fetching user information")
        return
    user_data = user_response.json()
    user_id = user_data['id']
    username = user_data['username']

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error fetching TODO list")
        return
    todos_data = todos_response.json()

    # Write data to CSV file
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for todo in todos_data:
            writer.writerow({'USER_ID': user_id,
                             'USERNAME': username,
                             'TASK_COMPLETED_STATUS': str(todo['completed']),
                             'TASK_TITLE': todo['title']})

