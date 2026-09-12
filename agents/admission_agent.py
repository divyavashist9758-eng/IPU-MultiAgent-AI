from dotenv import load_dotenv
from rag.retriever import retrieve
from utils.llm import generate_answer

load_dotenv()


def admission_agent(query):
    results = retrieve(query, 5)

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    if not documents:
        return "I could not find relevant admission information in the available IPU documents."

    context_parts = []

    for document, metadata in zip(documents, metadatas):
        source = metadata.get("source", "Unknown")
        page = metadata.get("page", "Unknown")

        context_parts.append(
            f"Source: {source} | Page: {page}\n{document}"
        )

    context = "\n\n---\n\n".join(context_parts)

    prompt = f"""You are an Admission Assistant for IPU students.

Answer the student's question using ONLY the information provided in the context below.

Rules:
- Do not invent or assume admission requirements.
- Do not use outside knowledge.
- If the answer is not present in the context, say that the information was not found in the available IPU documents.
- Give a clear and concise answer.
- Mention eligibility criteria, qualifications, exams, marks, documents, or conditions only when explicitly present in the context.
- At the end, mention the relevant source and page.

Student Question:
{query}

Context:
{context}

Answer:
"""

    return generate_answer(prompt)
