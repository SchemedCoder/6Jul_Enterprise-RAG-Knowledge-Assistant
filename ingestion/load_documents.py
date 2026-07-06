import os
from pathlib import Path

from ingestion.pdf_loader import load_pdf
from ingestion.text_cleaner import clean_text


RAW_FOLDER = "data/raw_docs"


def load_text_file(file_path):

    with open(file_path, "r", encoding="utf-8") as file:

        text = file.read()

    return {
        "file_name": Path(file_path).name,
        "document_type": "TEXT",
        "text": text
    }


def load_all_documents():

    documents = []

    for file in os.listdir(RAW_FOLDER):

        full_path = os.path.join(RAW_FOLDER, file)

        if file.endswith(".pdf"):

            document = load_pdf(full_path)

        elif file.endswith(".txt"):

            document = load_text_file(full_path)

        else:

            continue

        document["text"] = clean_text(document["text"])

        documents.append(document)

    return documents


if __name__ == "__main__":

    docs = load_all_documents()

    print("=" * 50)

    print("Loaded Documents")

    print("=" * 50)

    for doc in docs:

        print(f"File : {doc['file_name']}")
        print(f"Type : {doc['document_type']}")
        print(f"Length : {len(doc['text'])} characters")
        print("-" * 50)
