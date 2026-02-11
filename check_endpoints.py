import requests
import json

BASE_URL = "http://localhost:8080"
AUTH_TOKEN = "19b6e9675a68942c7c64b18ae694838c18767cd796a68b57e147df644d1a7f8b"

HEADERS = {
    "Authorization": AUTH_TOKEN,
    "Content-Type": "application/json"
}

# Try different endpoints to understand the API
endpoints = [
    "/api/v1/",
    "/api/v1/index/docs_index",
    "/api/v1/index/docs_index/info",
    "/api/v1/index/docs_index/vector/get",
]

for endpoint in endpoints:
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", headers=HEADERS)
        print(f"\n=== GET {endpoint} ===")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            try:
                print(json.dumps(response.json(), indent=2))
            except:
                print(f"Raw: {response.text[:200]}...")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Failed: {e}")

# Try POST to get vector by ID
print(f"\n=== POST to get vector by ID ===")
try:
    get_payload = {
        "id": "b5ffa306-97b7-482d-9bfd-0d2953bf5b69"  # Use an ID from our search results
    }
    response = requests.post(f"{BASE_URL}/api/v1/index/docs_index/vector/get", json=get_payload, headers=HEADERS)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        try:
            print(json.dumps(response.json(), indent=2))
        except:
            print(f"Raw: {response.text[:500]}...")
    else:
        print(f"Error: {response.text}")
except Exception as e:
    print(f"Failed: {e}")
