import csv
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
    filename = "{}.csv".format(employee_id)

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for todo in todos:
            writer.writerow({'USER_ID': employee_id,
                             'USERNAME': employee_name,
                             'TASK_COMPLETED_STATUS': str(todo['completed']),
                             'TASK_TITLE': todo['title']})
