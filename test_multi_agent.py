from app.orchestrator import run_multi_agent

questions = [
    "What are the passing marks for B.Tech?",
    "What is the Prime Minister Internship Scheme?"
]

for question in questions:
    print("\n" + "=" * 60)
    print("QUESTION:", question)
    print("=" * 60)
    print(run_multi_agent(question))
