import faiss
import numpy as np
import pickle
import os

INDEX_PATH = "faiss_index"

INDEX_FILE = os.path.join(INDEX_PATH, "index.faiss")
METADATA_FILE = os.path.join(INDEX_PATH, "metadata.pkl")


def create_vector_store(embeddings, chunks):

    os.makedirs(INDEX_PATH, exist_ok=True)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings).astype("float32"))

    faiss.write_index(index, INDEX_FILE)

    with open(METADATA_FILE, "wb") as file:

        pickle.dump(chunks, file)

    print("Vector database created successfully.")


def load_vector_store():

    index = faiss.read_index(INDEX_FILE)

    with open(METADATA_FILE, "rb") as file:

        metadata = pickle.load(file)

    return index, metadata
