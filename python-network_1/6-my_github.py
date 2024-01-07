import requests
import sys
from requests.auth import HTTPBasicAuth
url = 'https://api.github.com/user'
github_username = sys.argv[1]
github_token = sys.argv[2]
auth = HTTPBasicAuth(github_username, github_token)
headers = {
    'Accept': 'application/vnd.github.v3+json'
}

response = requests.get(url, auth=auth, headers=headers)

if response.status_code == 200:
    user_data = response.json()
    print(f"{user_data['id']}")
else:
    print(response.json())
