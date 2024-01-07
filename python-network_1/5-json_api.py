"""
 this module we will import requests and sys
"""
import requests
import sys
url = 'http://0.0.0.0:5000/search_user'
if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q = ""
response = requests.post(url, data={'q': q})
if response.status_code == 200:
    try:
        json_response = response.json()
        if json_response and 'id' in json_response and 'name' in json_response:
            user_id = json_response['id']
            user_name = json_response['name']
            print(f"[{user_id}] {user_name}")
        else:
            print("No result") 
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
else:
    print(f"error, {response.status_code}")
 