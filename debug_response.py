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
    "k": 3,
    "include_vectors": False
}

response = requests.post(
    f"{BASE_URL}/api/v1/index/{INDEX_NAME}/search",
    json=search_payload,
    headers=HEADERS
)

if response.status_code == 200:
    results = msgpack.unpackb(response.content, raw=False)
    print("Response structure:")
    print(f"Type: {type(results)}")
    print(f"Length: {len(results) if hasattr(results, '__len__') else 'N/A'}")
    
    if isinstance(results, list):
        for i, item in enumerate(results):
            print(f"\nResult {i}:")
            print(f"  Type: {type(item)}")
            print(f"  Length: {len(item) if hasattr(item, '__len__') else 'N/A'}")
            if isinstance(item, list):
                for j, subitem in enumerate(item):
                    print(f"    Item {j}: {subitem} (type: {type(subitem)})")
            else:
                print(f"  Value: {item}")
    else:
        print(f"Value: {results}")
