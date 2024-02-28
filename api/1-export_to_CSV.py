import csv
import sys
import requests

def get_todo_progress(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error fetching user information")
        return
    user_data = user_response.json()
    username = user_data["username"]

    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error fetching todo list")
        return
    todos_data = todos_response.json()

    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for todo in todos_data:
            writer.writerow(
                {
                    "USER_ID": employee_id,
                    "USERNAME": username,
                    "TASK_COMPLETED_STATUS": str(todo["completed"]),
                    "TASK_TITLE": todo["title"],
                }
            )

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_todo_progress(employee_id)