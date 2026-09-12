from utils.llm import generate_answer
from rag.retriever import retrieve


def academic_agent(query):
    results = retrieve(query, 5)

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    if not documents:
        return "I could not find relevant information in the available IPU documents."

    context_parts = []

    for document, metadata in zip(documents, metadatas):
        source = metadata.get("source", "Unknown")
        page = metadata.get("page", "Unknown")

        context_parts.append(
            f"Source: {source} | Page: {page}\n{document}"
        )

    context = "\n\n---\n\n".join(context_parts)

    prompt = f"""You are an Academic Assistant for IPU students.

Answer the student's question using ONLY the information provided in the context below.

Rules:
- Do not invent or assume information.
- If the answer is not present in the context, say that the information was not found in the available documents.
- Give a clear and concise answer.
- Mention important rules, marks, percentages, or conditions exactly as stated in the documents.
- At the end, provide the relevant source and page.

Student Question:
{query}

Context:
{context}

Answer:
"""

    return generate_answer(prompt)

