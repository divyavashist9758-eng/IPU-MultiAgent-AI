import chromadb

DB_PATH = "chroma_db"
COLLECTION_NAME = "ipu_documents"

client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)


def add_documents(documents, ids, metadatas):
    collection.upsert(
        documents=documents,
        ids=ids,
        metadatas=metadatas
    )


def search_documents(query, n_results=5, where=None):
    kwargs = {
        "query_texts": [query],
        "n_results": n_results
    }

    if where:
        kwargs["where"] = where

    return collection.query(**kwargs)
