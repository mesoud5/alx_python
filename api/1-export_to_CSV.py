#!/usr/bin/python3

import sys
import requests
import csv

def get_TODOlist(employee_id):
    endpoint = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    response = requests.get(endpoint)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error: Failed to make successful request")
        return None, None

def export_to_CSV(employee_id, employee_name, tasks):
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': task['completed'],
                'TASK_TITLE': task['title']
            })
    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    employee_id = sys.argv[1]

    employee_data, tasks = get_TODOlist(employee_id)

    if employee_data and tasks:
        employee_name = employee_data[0]['name']
        export_to_CSV(employee_id, employee_name, tasks)
    else:
        print("Error: No data retrieved from the URL")
