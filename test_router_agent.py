from agents.router_agent import router_agent

questions = [
    "What are the passing marks for B.Tech?",
    "Tell me about the Prime Minister Internship Scheme.",
    "What are the rules for rechecking an examination?",
    "What university notices are available about internships?"
]

for question in questions:
    print("\nQuestion:", question)
    print("Route:", router_agent(question))
