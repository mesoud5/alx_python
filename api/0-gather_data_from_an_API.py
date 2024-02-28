import requests
import sys


def get_employee_data(employee_id):
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    return employee_data

def get_employee_todos(employee_id):
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    return todos_data

def display_employee_todo_progress(employee_id):
    employee_data = get_employee_data(employee_id)
    employee_name = employee_data["name"]
    todos_data = get_employee_todos(employee_id)
    done_tasks = [todo for todo in todos_data if todo["completed"]]
    total_tasks = len(todos_data)
    done_tasks_count = len(done_tasks)

    # Print the employee name and progress
    print(f"Employee {employee_name} is done with tasks({done_tasks_count}/{total_tasks}):")

    # Print the titles of the completed tasks with formatting evaluation
    for i, task in enumerate(done_tasks, 1):
        task_title = task['title']
        expected_format = f"Task {i} Formatting: OK"
        actual_format = f"Task {i} Formatting: {'OK' if task_title == expected_format else 'Incorrect'}"
        print(f"\t{actual_format}")

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    display_employee_todo_progress(employee_id)
