import ollama

client = ollama.Client()

def get_answer(question):
    
    model = "gemma3"
    prompt =  question +"Answer with yes or no."

    response = client.generate(model=model, prompt=prompt)

    return response