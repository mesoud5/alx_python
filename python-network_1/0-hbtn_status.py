import requests
url = 'https://alu-intranet.hbtn.io/status'
response = requests.get(url)
Type = {type(response.text)}
print("Body response")
print("    - type:", Type)
content = response.text
print("    - content:", content)
