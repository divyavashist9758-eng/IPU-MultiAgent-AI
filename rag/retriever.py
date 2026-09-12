from rag.vectorstore import search_documents


def retrieve(query, n_results=5):
    results = search_documents(query, n_results)

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    filtered_documents = []
    filtered_metadatas = []
    filtered_distances = []

    for document, metadata, distance in zip(
        documents, metadatas, distances
    ):
        if distance <= 1.5:
            filtered_documents.append(document)
            filtered_metadatas.append(metadata)
            filtered_distances.append(distance)

    return {
        "documents": [filtered_documents],
        "metadatas": [filtered_metadatas],
        "distances": [filtered_distances],
    }
