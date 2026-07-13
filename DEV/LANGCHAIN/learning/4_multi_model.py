from langchain_community.chat_models import ollama

model = ollama.ChatOllama(
    model='gemma3:latest',
    temperature=0.7,
)
print(model.invoke('Hello').content)

model2 = ollama.ChatOllama(
    model='gemma1:latest',
    temperature=0.7,
)
print(model2.invoke('Hello').content)