from sentence_transformers import SentenceTransformer

from embeddings.vector_store import load_vector_store

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def search(query, top_k=5):

    index, metadata = load_vector_store()

    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding.astype("float32"), top_k)

    results = []

    for idx in indices[0]:

        results.append(metadata[idx])

    return results


if __name__ == "__main__":

    question = "What is the leave policy?"

    answers = search(question)

    for item in answers:

        print("=" * 50)
        print(item["file_name"])
        print(item["text"])
