from embeddings.search import search

from llm.prompt_template import SYSTEM_PROMPT
from llm.answer_generator import generate_answer


def ask_question(question):

    retrieved_chunks = search(
        question,
        top_k=5
    )

    context = "\n\n".join(
        chunk["text"]
        for chunk in retrieved_chunks
    )

    prompt = SYSTEM_PROMPT.format(
        context=context,
        question=question
    )

    answer = generate_answer(prompt)

    return {
        "question": question,
        "answer": answer,
        "sources": [
            chunk["file_name"]
            for chunk in retrieved_chunks
        ]
    }


if __name__ == "__main__":

    result = ask_question(
        "What is the leave policy?"
    )

    print(result)
