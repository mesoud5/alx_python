import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit()

    employee_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    response = requests.get(url)
    todos = response.json()

    user_info_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_info_response = requests.get(user_info_url)
    user_info = user_info_response.json()

    employee_name = user_info['username']
    tasks = []

    for todo in todos:
        task_info = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": employee_name
        }
        tasks.append(task_info)

    filename = "{}.json".format(employee_id)
    with open(filename, 'w') as json_file:
        json.dump({employee_id: tasks}, json_file)
