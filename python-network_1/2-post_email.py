"""
in this module we will import requests and sys
"""
import requests
import sys
url = sys.argv[1]
email = sys.argv[2]
response = requests.get(url)
posting = response.post(email)
print(posting.text)