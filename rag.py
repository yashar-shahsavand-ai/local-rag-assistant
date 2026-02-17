import chromadb
from llm import generate
from embedder import embed

client = chromadb.Client()
collection = client.get_or_create_collection("knowledge")

def ask(question):
q_embedding = embed([question])[0]

```
results = collection.query(
    query_embeddings=[q_embedding],
    n_results=3
)

context = "\n".join(results["documents"][0])

prompt = f"""
```

You are an internal company assistant.
Answer only based on the provided context.

Context:
{context}

Question:
{question}

If the answer is not in the context, say you don't know.
"""

```
return generate(prompt)
```
