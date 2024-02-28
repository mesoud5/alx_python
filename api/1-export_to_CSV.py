#!/usr/bin/env python3
"""
Export to CSV
"""
import sys
import csv
import requests


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


def export_to_csv(employee_id, user_data, todos_data):
    """
    Exports data to CSV format
    """
    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos_data:
            writer.writerow([employee_id, user_data['username'], todo['completed'], todo['title']])

    print(f"Data exported to {filename}")


def main():
    """
    Main function
    """
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_data, todos_data = fetch_data(employee_id)
    export_to_csv(employee_id, user_data, todos_data)


if __name__ == "__main__":
    main()
