from dotenv import load_dotenv

from utils.llm import generate_answer
from rag.retriever import retrieve

load_dotenv()


def student_services_agent(query):
    results = retrieve(query, 5)

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    if not documents:
        return "I could not find relevant student services information in the available IPU documents."

    context_parts = []

    for document, metadata in zip(documents, metadatas):
        source = metadata.get("source", "Unknown")
        page = metadata.get("page", "Unknown")
        context_parts.append(
            f"Source: {source} | Page: {page}\n{document}"
        )

    context = "\n\n---\n\n".join(context_parts)

    prompt = f"""You are a Student Services Assistant for IPU students.

Answer the student's question using ONLY the information provided in the context below.

Rules:
- Do not invent or assume information.
- Do not use outside knowledge.
- If the answer is not present in the context, say that the information was not found in the available IPU documents.
- Give a clear and concise answer.
- If the context contains a procedure, explain the steps clearly.
- Mention important fees, forms, deadlines, conditions, or requirements only when explicitly present.
- At the end, mention the relevant source and page.

Student Question:
{query}

Context:
{context}

Answer:
"""

    return generate_answer(prompt)
