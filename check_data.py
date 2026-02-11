import requests
import msgpack
import json

BASE_URL = "http://localhost:8080"
INDEX_NAME = "docs_index"
AUTH_TOKEN = "19b6e9675a68942c7c64b18ae694838c18767cd796a68b57e147df644d1a7f8b"

HEADERS = {
    "Authorization": AUTH_TOKEN,
    "Content-Type": "application/json"
}

# Get index info
response = requests.get(
    f"{BASE_URL}/api/v1/index/{INDEX_NAME}/info",
    headers=HEADERS
)

print("Index Info:")
print(f"Status: {response.status_code}")
print(f"Content-Type: {response.headers.get('content-type')}")

if response.status_code == 200:
    if response.headers.get('content-type') == 'application/msgpack':
        info = msgpack.unpackb(response.content, raw=False)
        print(json.dumps(info, indent=2, default=str))
    else:
        print(response.text)
else:
    print(f"Error: {response.text}")
