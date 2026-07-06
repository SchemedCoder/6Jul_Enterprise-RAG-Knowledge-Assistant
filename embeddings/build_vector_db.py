from ingestion.load_documents import load_all_documents
from embeddings.chunking import chunk_documents
from embeddings.create_embeddings import generate_embeddings
from embeddings.vector_store import create_vector_store


def build():

    print("Loading documents...")

    docs = load_all_documents()

    print(f"{len(docs)} documents loaded.")

    print("Creating chunks...")

    chunks = chunk_documents(docs)

    print(f"{len(chunks)} chunks created.")

    print("Generating embeddings...")

    embeddings = generate_embeddings(chunks)

    print("Saving FAISS index...")

    create_vector_store(embeddings, chunks)

    print("Completed successfully.")


if __name__ == "__main__":

    build()
