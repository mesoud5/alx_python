#!/usr/bin/python3
"""
Script that takes GitHub credentials and uses the GitHub API to display the user ID
"""

import sys
import requests

def get_github_user_id(username, token):
    url = "https://api.github.com/user"
    auth = (username, token)
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        return response.json().get("id")
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-my_github.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    user_id = get_github_user_id(username, token)

    print(user_id)
