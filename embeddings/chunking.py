from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_documents(documents):
    """
    Split documents into overlapping chunks for semantic search.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = []

    for document in documents:

        split_text = splitter.split_text(document["text"])

        for i, text in enumerate(split_text):

            chunks.append(
                {
                    "file_name": document["file_name"],
                    "document_type": document["document_type"],
                    "chunk_id": i,
                    "text": text
                }
            )

    return chunks
