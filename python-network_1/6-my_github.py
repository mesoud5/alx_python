import requests
import sys
import base64

url = 'https://api.github.com/user'
github_username = sys.argv[1]
github_token = sys.argv[2]

credentials = base64.b64encode(f"{github_username}:{github_token}".encode('utf-8')).decode('utf-8')
headers = {
    'Authorization': f"Basic {credentials}",
    'Accept': 'application/vnd.github.v3+json'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    user_data = response.json()
    print(f"{user_data['id']}")
else:
    print(response.json())
