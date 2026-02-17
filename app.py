from fastapi import FastAPI
from rag import ask

app = FastAPI()

@app.get("/ask")
def query(q: str):
answer = ask(q)
return {"answer": answer}
