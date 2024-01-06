import requests
url = 'https://alu-intranet.hbtn.io/status'
response = requests.get(url)
print("Body response:")
print(f"\t- type: {type(response.text)}")
print(f"\t- content: {response.text}")
