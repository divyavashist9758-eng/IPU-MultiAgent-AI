import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing from .env")

client = Groq(
    api_key=GROQ_API_KEY
)

DEFAULT_MODEL = "qwen/qwen3.8-27b"


def generate_answer(prompt, model=DEFAULT_MODEL, temperature=0.2, max_tokens=512):
    """
    Centralized Groq LLM completion function for all agents.
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content
