#!/usr/bin/python3


import sys
import requests

def get_TODOlist(employee_id):
    endpoint = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    
    response = requests.get(endpoint)

    if response.status_code == 200:
        user_data = response.json()
        return user_data.get("name"), user_data.get("todos")
    else:
        print("error: failed to make succesful request")
        return None, None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("below or above 2 argument including the script name")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    employee_name, todo_list = get_TODOlist(employee_id)

    if employee_name and todo_list:
        total_tasks = len(todo_list)
        done_tasks = sum(1 for todo in todo_list if todo["completed"])
        print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks})")

        for todo in todo_list:
            if todo["completed"]:
                print(f"\t{todo['title']}")
    else:
        print("Error: No data retrieved from the url mesoud")
    
