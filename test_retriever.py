from rag.retriever import retrieve

results = retrieve("What are the examination rules for B.Tech students?", 3)

print(results)
