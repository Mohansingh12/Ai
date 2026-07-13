from langchain_ollama import chat_models as ollama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

chat_history = []
chat_history.append(SystemMessage(content="You are a helpful assistant."))
    
model = ollama.ChatOllama(
    model='gemma3:latest',
    temperature=0.7,
    
)


while True:
    message = input("You: ")

    chat_history.append(HumanMessage(content=message))
    response = model.invoke(chat_history)
    print(response.content)
    chat_history.append(AIMessage(content=response.content))
    if message.lower() in ['exit', 'quit']:
        print("Exiting the chatbot. Goodbye!")
        break

