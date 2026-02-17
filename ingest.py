import os
import chromadb
from embedder import embed

CHUNK_SIZE = 400
CHUNK_OVERLAP = 50

def chunk_text(text):
chunks = []
start = 0
while start < len(text):
end = start + CHUNK_SIZE
chunks.append(text[start:end])
start += CHUNK_SIZE - CHUNK_OVERLAP
return chunks

def ingest_folder(path="data/sample_docs"):
client = chromadb.Client()
collection = client.get_or_create_collection("knowledge")

```
for file in os.listdir(path):
    with open(os.path.join(path, file), "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text)
    embeddings = embed(chunks)

    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            embeddings=[embeddings[i]],
            ids=[f"{file}_{i}"]
        )

print("Ingestion complete.")
```

if **name** == "**main**":
ingest_folder()
