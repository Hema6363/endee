import requests
import msgpack
import json

BASE_URL = "http://localhost:8080"
AUTH_TOKEN = "19b6e9675a68942c7c64b18ae694838c18767cd796a68b57e147df644d1a7f8b"

HEADERS = {
    "Authorization": AUTH_TOKEN,
    "Content-Type": "application/json"
}

# Get vector by ID
get_payload = {
    "id": "b5ffa306-97b7-482d-9bfd-0d2953bf5b69"
}

response = requests.post(f"{BASE_URL}/api/v1/index/docs_index/vector/get", json=get_payload, headers=HEADERS)

if response.status_code == 200:
    # Try to decode as MessagePack
    try:
        result = msgpack.unpackb(response.content, raw=False)
        print("Decoded MessagePack:")
        print(json.dumps(result, indent=2, default=str))
        
        # If it's a list, show structure
        if isinstance(result, list):
            print(f"\nResult type: {type(result)}")
            print(f"Result length: {len(result)}")
            for i, item in enumerate(result):
                print(f"  Item {i}: {type(item)} - {repr(item)[:100]}...")
                
    except Exception as e:
        print(f"Failed to decode MessagePack: {e}")
        print(f"Raw bytes (first 100): {response.content[:100]}")
else:
    print(f"Error: {response.status_code} - {response.text}")
