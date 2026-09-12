from dotenv import load_dotenv

from utils.llm import generate_answer
from rag.retriever import retrieve

load_dotenv()


def notice_agent(query):
    results = retrieve(query, 5)

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    if not documents:
        return "I could not find any relevant notice in the available documents."

    context_parts = []

    for document, metadata in zip(documents, metadatas):
        source = metadata.get("source", "Unknown")
        page = metadata.get("page", "Unknown")
        context_parts.append(
            f"Source: {source} | Page: {page}\n{document}"
        )

    context = "\n\n---\n\n".join(context_parts)

    prompt = f"""You are a Notice and Circular Assistant for IPU students.

Answer the student's question using ONLY the notice information provided in the context.

Rules:
- Do not invent notice dates, deadlines, events, or instructions.
- If the requested information is not present, clearly say that it was not found.
- Focus on notices, circulars, announcements, deadlines, applications, examinations, internships, and university instructions.
- Give a concise and student-friendly answer.
- At the end, mention the relevant source and page.

Student Question:
{query}

Notice Context:
{context}

Answer:
"""

    return generate_answer(prompt)
