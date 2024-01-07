import requests
import sys

url = 'https://api.github.com/user'
github_username = sys.argv[1]
github_token = sys.argv[2]

headers = {
    'Autorization': f"{github_username}:{github_token}",
    'Accept': 'application/vnd.github.v3+json'
}
response = requests.get(url, headers=headers)
user_data = response.json()
print(f"{user_data['id']}")