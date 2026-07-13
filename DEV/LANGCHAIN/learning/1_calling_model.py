from langchain_community.chat_models import openai

model=openai.ChatOpenAI(
    model ='gemma3',
    base_url= 'http://localhost:11434',
    temperature=0.7,
    api_key='no_required'
)
response=model.invoke('Hello')