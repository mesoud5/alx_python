#!/usr/bin/env python3
"""
Dictionary of list of dictionaries
"""
import json
import requests


def fetch_all_data():
    """
    Fetches data of all employees
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_response = requests.get(f'{base_url}/users')
    users_data = user_response.json()

    all_data = {}
    for user in users_data:
        todos_response = requests.get(f'{base_url}/todos?userId={user["id"]}')
        todos_data = todos_response.json()
        all_data[user['id']] = {
            "username": user["username"],
            "tasks": [{"task": todo["title"], "completed": todo["completed"]} for todo in todos_data]
        }

    return all_data


def main():
    """
    Main function
    """
    all_data = fetch_all_data()

    with open("todo_all_employees.json", mode='w') as file:
        json.dump(all_data, file)

    print("Data exported to todo_all_employees.json")


if __name__ == "__main__":
    main()
