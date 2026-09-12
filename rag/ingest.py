import os
from pypdf import PdfReader

from rag.vectorstore import add_documents

DATA_DIR = "data"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


def split_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):

    text = text.strip()

    if not text:
        return []

    chunks = []
    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def load_pdfs():

    documents = []
    ids = []
    metadatas = []

    counter = 0

    for root, _, files in os.walk(DATA_DIR):

        for file in files:

            if not file.lower().endswith(".pdf"):
                continue

            path = os.path.join(root, file)

            try:

                reader = PdfReader(path)

                for page_number, page in enumerate(reader.pages):

                    text = page.extract_text()

                    if not text or not text.strip():
                        continue

                    chunks = split_text(text)

                    for chunk_number, chunk in enumerate(chunks):

                        documents.append(chunk)

                        ids.append(
                            f"doc_{counter}"
                        )

                        metadatas.append({
                            "source": path,
                            "page": page_number + 1,
                            "chunk": chunk_number + 1
                        })

                        counter += 1

            except Exception as e:

                print(f"Error reading {path}: {e}")

    return documents, ids, metadatas


if __name__ == "__main__":

    documents, ids, metadatas = load_pdfs()

    print(f"Chunks created: {len(documents)}")

    if documents:

        add_documents(
            documents,
            ids,
            metadatas
        )

        print("Documents successfully added to ChromaDB.")

    else:

        print("No PDF text was extracted.")
