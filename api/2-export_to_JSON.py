#!/usr/bin/env python3
"""
Export to JSON
"""
import json
import requests
import sys


def fetch_data(employee_id):
    """
    Fetches data from the given employee ID
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')

    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data


def export_to_json(employee_id, user_data, todos_data):
    """
    Exports data to JSON format
    """
    data = {str(employee_id): [{"task": todo['title'], "completed": todo['completed'], "username": user_data['username']} for todo in todos_data]}
    filename = f"{employee_id}.json"

    with open(filename, mode='w') as file:
        json.dump(data, file)

    print(f"Data exported to {filename}")


def main():
    """
    Main function
    """
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_data, todos_data = fetch_data(employee_id)
    export_to_json(employee_id, user_data, todos_data)


if __name__ == "__main__":
    main()
