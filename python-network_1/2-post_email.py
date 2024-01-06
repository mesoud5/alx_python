"""
in this module we will import requests and sys
"""
import requests
import sys
url = sys.argv[1]
email = sys.argv[2]
response = requests.post(url, data={'email': email})

print(response.text)