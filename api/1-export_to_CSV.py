import csv
import requests
import sys

def get_user_info(employee_id):
    """Fetch user information from the API."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    try:
        response = requests.get(user_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching user information: {e}")
        sys.exit(1)

def get_todo_list(employee_id):
    """Fetch TODO list for the specified employee ID."""
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    try:
        response = requests.get(todos_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching TODO list: {e}")
        sys.exit(1)

def export_to_csv(user_info, todo_list):
    """Export user's TODO list to a CSV file."""
    user_id = user_info['id']
    username = user_info['username']
    csv_filename = f"{user_id}.csv"

    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todo_list:
            csv_writer.writerow([user_id, username, todo["completed"], todo["title"]])

    print(f"Data exported to '{csv_filename}' successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        if employee_id <= 0:
            raise ValueError("Employee ID must be a positive integer")
    except (ValueError, TypeError):
        print("Employee ID must be a positive integer")
        sys.exit(1)

    user_info = get_user_info(employee_id)
    todo_list = get_todo_list(employee_id)
    export_to_csv(user_info, todo_list)
