import requests
import sys

# Get the URL from the command-line argument
url = sys.argv[1]

# Send an HTTP request to the provided URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Retrieve and display X-Request-Id header value
    request_id = response.headers.get('X-Request-Id')
    if request_id:
        print(request_id)
    else:
        print(None)

else:
    print(f"Failed to make the request. Status code: {response.status_code}")
