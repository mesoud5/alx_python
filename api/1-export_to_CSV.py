import csv
import requests
import sys

def get_todo_progress(employee_id):
    # Define API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch user information
    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()  # Raise exception for non-200 status codes
        user_data = user_response.json()
        username = user_data['username']
    except requests.RequestException as e:
        print(f"Error fetching user information: {e}")
        sys.exit(1)

    # Fetch TODO list
    try:
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()  # Raise exception for non-200 status codes
        todos_data = todos_response.json()
    except requests.RequestException as e:
        print(f"Error fetching TODO list: {e}")
        sys.exit(1)

    # Write data to CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos_data:
            csv_writer.writerow([employee_id, username, todo["completed"], todo["title"]])

    print(f"Data exported to '{csv_filename}' successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        if employee_id <= 0:
            raise ValueError("Employee ID must be a positive integer")
    except ValueError:
        print("Employee ID must be a positive integer")
        sys.exit(1)

    get_todo_progress(employee_id)
