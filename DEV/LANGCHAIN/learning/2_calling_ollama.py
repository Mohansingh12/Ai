from langchain_community.chat_models import ollama

model = ollama.ChatOllama(
    model='gemma3:latest',
    temperature=0.7,
)
response = model.invoke('Hello')