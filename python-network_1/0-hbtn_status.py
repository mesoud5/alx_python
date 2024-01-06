import requests
url = 'https://alu-intranet.hbtn.io/status'
response = requests.get(url)
print("Body response:")
print(f"    - type: {type(response.text)}")
print(f"    - content: {response.text}")
