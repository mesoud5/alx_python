import requests
url = 'https://alu-intranet.hbtn.io/status'
response = requests.get(url)
Type = {type(response.text)}
print("Body response:")
print(f"    - type:{Type}")
content = response.text
print(f"    - content:{content}")
