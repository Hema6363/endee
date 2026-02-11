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

search_payload = {
    "vector": [0.1] * 384,
    "k": 1,
    "include_vectors": True
}

response = requests.post(
    f"{BASE_URL}/api/v1/index/{INDEX_NAME}/search",
    json=search_payload,
    headers=HEADERS
)

if response.status_code == 200:
    results = msgpack.unpackb(response.content, raw=False)
    print("Detailed response analysis:")
    for i, result in enumerate(results):
        print(f"\nResult {i}:")
        for j, item in enumerate(result):
            print(f"  Position {j}: {repr(item)} (type: {type(item).__name__})")
            # If it's bytes, try to decode
            if isinstance(item, bytes):
                try:
                    decoded = item.decode('utf-8')
                    print(f"    Decoded: {repr(decoded)}")
                except:
                    print(f"    Cannot decode as UTF-8")
else:
    print(f"Error: {response.status_code} - {response.text}")
