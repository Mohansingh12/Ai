from langchain_community.chat_models import ollama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

model = ollama.ChatOllama(
    model='gemma3', 
    temperature=0.7,
)
prompt = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hello"),
    ]
response = model.invoke(prompt)
print(response.content)

prompt1 = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content=response.content),
    ]
response = model.invoke(prompt1)
print(response.content)