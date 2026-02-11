import requests
import uuid
from sentence_transformers import SentenceTransformer
import msgpack
import json

BASE_URL = "http://localhost:8080"
INDEX_NAME = "docs_index"
AUTH_TOKEN = "19b6e9675a68942c7c64b18ae694838c18767cd796a68b57e147df644d1a7f8b"

HEADERS = {
    "Authorization": AUTH_TOKEN,
    "Content-Type": "application/json"
}

model = SentenceTransformer("all-MiniLM-L6-v2")

# Load documents
with open("sample_docs.txt", "r") as f:
    docs = [line.strip() for line in f if line.strip()]

print(f"Found {len(docs)} documents")

# Create vectors with proper metadata
vectors = []
for i, doc in enumerate(docs):
    vector = model.encode(doc).tolist()
    vectors.append({
        "id": str(uuid.uuid4()),
        "vector": vector,
        "metadata": doc,  # Store text directly as metadata
        "filter": {
            "source": "demo"
        }
    })
    print(f"Document {i+1}: {doc[:50]}...")

print(f"\nInserting {len(vectors)} vectors...")

insert_response = requests.post(
    f"{BASE_URL}/api/v1/index/{INDEX_NAME}/vector/insert",
    json=vectors,
    headers=HEADERS
)

print(f"Insert Status: {insert_response.status_code}")

# Handle response
try:
    if insert_response.headers.get('content-type') == 'application/msgpack':
        result = msgpack.unpackb(insert_response.content, raw=False)
        print("Insert Response:", json.dumps(result, indent=2, default=str))
    else:
        print("Insert Response:", insert_response.text)
except Exception as e:
    print("Insert Response:", insert_response.text)
