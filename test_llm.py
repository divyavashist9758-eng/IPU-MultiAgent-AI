from dotenv import load_dotenv
import os

from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN"),
    provider="auto"
)

response = client.chat.completions.create(
    model="Qwen/Qwen3-8B",
    messages=[
        {
            "role": "user",
            "content": "What is artificial intelligence? Explain in one sentence."
        }
    ],
)

print("\nLLM RESPONSE:")
print(response.choices[0].message.content)
