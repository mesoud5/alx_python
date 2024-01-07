import requests
import sys

url = 'https://api.github.com/user'
github_username = sys.argv[1]
github_token = sys.argv[2]

headers = {
    'Authorization': f"Bearer {github_token}",
    'Accept': 'application/vnd.github.v3+json'
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    user_data = response.json()
    print(f"{user_data['id']}")
else:
    print(response.json())
