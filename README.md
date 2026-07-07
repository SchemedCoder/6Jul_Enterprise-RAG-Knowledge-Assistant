# Enterprise RAG Knowledge Assistant

## Overview

An enterprise Retrieval-Augmented Generation (RAG) platform that enables intelligent question answering over internal company documents using semantic search and Large Language Models.

---

## Features

- PDF & Text document ingestion
- Intelligent document chunking
- Sentence Transformer embeddings
- FAISS vector search
- LLM-powered grounded responses
- FastAPI REST APIs
- Streamlit Dashboard
- Automated Evaluation
- GitHub Actions CI/CD

---

## Architecture

Documents
    ↓
Ingestion
    ↓
Cleaning
    ↓
Chunking
    ↓
Embeddings
    ↓
FAISS Vector Store
    ↓
Similarity Search
    ↓
LLM
    ↓
Grounded Answer

---

## Tech Stack

- Python
- FastAPI
- LangChain
- OpenAI
- Sentence Transformers
- FAISS
- Streamlit
- GitHub Actions
- PyPDF

---

## Folder Structure

See repository tree for complete architecture.

---

## Future Enhancements

- Azure AI Search
- ChromaDB
- Redis Cache
- Azure OpenAI
- Multi-document conversations


## Question Answering API

The application exposes a FastAPI endpoint for semantic document search.

### Endpoint

POST `/ask`

Example request:

```json
{
  "question": "What is the leave policy?"
}
```

Example response:

```json
{
  "question": "What is the leave policy?",
  "answer": "...",
  "sources": [
    "employee_handbook.txt"
  ]
}
```
