
from langchain_community.llms import OpenAI
import requests

BASE_URL = "http://localhost:1234"

# Check if the local LLM server is running
try:
    requests.get(BASE_URL, timeout=3)
except Exception as e:
    print(f"Error: Could not connect to LLM server at {BASE_URL}. Is it running?\n{e}")
    exit(1)

try:
    chat = OpenAI(
        base_url=BASE_URL,
        api_key="not-needed",
        model="qwen/qwen3-4b-thinking-2507"
    )
    response = chat.invoke("Tell me a joke")
    print(response)
except Exception as e:
    print(f"Error during chat invocation: {e}")
