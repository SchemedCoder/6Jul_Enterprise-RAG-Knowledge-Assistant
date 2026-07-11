# Enterprise RAG Knowledge Assistant

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)
![LangChain](https://img.shields.io/badge/LangChain-RAG-blueviolet)
![FAISS](https://img.shields.io/badge/Vector_DB-FAISS-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Overview

Enterprise Retrieval-Augmented Generation (RAG) platform that enables intelligent semantic search and grounded question answering over enterprise knowledge bases using FastAPI, LangChain, FAISS, and Sentence Transformers.

This project demonstrates an end-to-end enterprise AI pipeline including document ingestion, preprocessing, vector database creation, semantic retrieval, and LLM-powered answer generation.

---

# Features

- Enterprise Retrieval-Augmented Generation (RAG)
- PDF & Text document ingestion
- Intelligent document preprocessing
- Recursive text chunking
- Sentence Transformer embeddings
- FAISS semantic vector search
- LangChain retrieval pipeline
- FastAPI REST APIs
- Streamlit dashboard (In Progress)
- Modular enterprise architecture
- Automated evaluation pipeline
- GitHub Actions CI/CD (Planned)
- Easily extensible to OpenAI or Azure OpenAI

---

# Architecture

```text
Enterprise Documents
        │
        ▼
Document Ingestion
        │
        ▼
Text Cleaning
        │
        ▼
Recursive Chunking
        │
        ▼
Sentence Embeddings
        │
        ▼
FAISS Vector Store
        │
        ▼
Similarity Search
        │
        ▼
LLM Context Generation
        │
        ▼
Grounded Answer
```

---

# Tech Stack

- Python
- FastAPI
- LangChain
- OpenAI
- Sentence Transformers
- FAISS
- Streamlit
- GitHub Actions
- PyPDF
- NumPy
- Pandas

---



---

# Quick Start

Clone the repository

```bash
git clone https://github.com/<your_username>/27-Enterprise-RAG-Knowledge-Assistant.git
```

Move into the project

```bash
cd 27-Enterprise-RAG-Knowledge-Assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Build the vector database

```bash
python -m embeddings.build_vector_db
```

Run the FastAPI server

```bash
uvicorn api.main:app --reload
```

Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

# Question Answering API

### Endpoint

```
POST /ask
```

### Example Request

```json
{
    "question": "What is the leave policy?"
}
```

### Example Response

```json
{
    "question": "What is the leave policy?",
    "answer": "Employees are entitled to 20 paid leaves annually.",
    "sources": [
        "employee_handbook.txt"
    ]
}
```

---

# Current Progress

| Module | Status |
|---------|--------|
| Document Ingestion | ✅ |
| Text Cleaning | ✅ |
| Recursive Chunking | ✅ |
| Embedding Generation | ✅ |
| FAISS Vector Database | ✅ |
| Semantic Retrieval | ✅ |
| FastAPI REST API | 🚧 |
| Streamlit Dashboard | 🚧 |
| Docker | 🚧 |
| GitHub Actions | 🚧 |

---

# Future Enhancements

- Azure OpenAI Integration
- Azure AI Search
- ChromaDB Support
- Redis Semantic Cache
- Multi-document Conversations
- Authentication & Authorization
- Docker Deployment
- CI/CD Pipeline
- Kubernetes Deployment

---

# Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Enterprise AI Architecture
- Semantic Search
- Vector Databases
- FastAPI Development
- LangChain
- Prompt Engineering
- Sentence Transformers
- Enterprise Python Development
- REST API Design
- Software Engineering Best Practices

---
