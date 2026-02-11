import requests
import json

BASE_URL = "http://localhost:8080"
INDEX_NAME = "docs_index"
AUTH_TOKEN = "19b6e9675a68942c7c64b18ae694838c18767cd796a68b57e147df644d1a7f8b"

HEADERS = {
    "Authorization": AUTH_TOKEN,
    "Content-Type": "application/json"
}

# Test search with a simple vector
search_payload = {
    "vector": [0.1] * 384,  # 384 dimensions to match the model
    "k": 3,
    "include_vectors": False
}

try:
    response = requests.post(
        f"{BASE_URL}/api/v1/index/{INDEX_NAME}/search",
        json=search_payload,
        headers=HEADERS
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Content-Type: {response.headers.get('content-type', 'Unknown')}")
    print(f"Content-Length: {len(response.content)}")
    
    if response.status_code == 200:
        print("\nRaw response (first 200 bytes):")
        print(response.content[:200])
        
        # Try to decode as JSON
        try:
            json_response = response.json()
            print("\nJSON response:")
            print(json.dumps(json_response, indent=2))
        except json.JSONDecodeError as e:
            print(f"\nFailed to decode as JSON: {e}")
            
            # Try to decode as MessagePack
            try:
                import msgpack
                msgpack_response = msgpack.unpackb(response.content, raw=False)
                print("\nMessagePack response:")
                print(json.dumps(msgpack_response, indent=2, default=str))
            except ImportError:
                print("\nMessagePack library not installed")
            except Exception as e:
                print(f"\nFailed to decode as MessagePack: {e}")
    else:
        print(f"\nError response: {response.text}")
        
except Exception as e:
    print(f"Request failed: {e}")
