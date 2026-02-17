# Local RAG Assistant (Fully Offline Private AI)

A fully local Retrieval-Augmented Generation (RAG) assistant designed for private company knowledge bases.
The system runs entirely offline and does not require OpenAI or cloud APIs, making it suitable for GDPR-sensitive environments.

## Features

* Fully local LLM inference via Ollama
* Document ingestion and chunking
* Semantic search using embeddings
* Vector database retrieval (ChromaDB)
* Context-aware answering
* FastAPI interface
* Works without internet after setup

## Use Case

Small and medium companies often cannot upload internal documents to cloud LLM providers.
This project demonstrates an on-premise knowledge assistant that can answer questions about company documentation, manuals, or internal procedures.

## Architecture

Documents → Chunking → Embedding → Vector DB → Retrieval → Prompt → Local LLM → Answer

## Setup

Install Ollama:
https://ollama.ai

Pull model:
ollama pull mistral

Install dependencies:
pip install -r requirements.txt

Ingest documents:
python ingest.py

Run server:
uvicorn app:app --reload

Open:
http://127.0.0.1:8000/docs

## Example Questions

* "How many vacation days do employees have?"
* "What is the IT password policy?"
* "Who should I contact for HR support?"

## Note

This repository is a clean-room demonstration recreating techniques used in real-world private AI deployments.
