from fastapi import FastAPI
from pydantic import BaseModel

from llm.rag_pipeline import ask_question

app = FastAPI(
    title="Enterprise RAG API"
)


class Question(BaseModel):
    question: str


@app.get("/")
def home():

    return {
        "message": "Enterprise RAG API Running"
    }


@app.post("/ask")
def ask(data: Question):

    return ask_question(data.question)
