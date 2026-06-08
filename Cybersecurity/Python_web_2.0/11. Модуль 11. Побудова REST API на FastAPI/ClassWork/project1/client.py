import requests
import json

data = {
    "title": "Test",
    "content": "Hello"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(
    "http://127.0.0.1:8000/notes",
    data=json.dumps(data),
    headers=headers
)

print(response.json())
