import ollama

client = ollama.Client()

def get_answer(question):
    
    model = "gemma3"
    prompt =  question +"Answer with yes or no."

    response = client.generate(model=model, prompt=prompt)

    # Normalize to a plain string ("Yes."/"No.") regardless of return shape
    if isinstance(response, dict):
        return response.get('response') or response.get('message') or str(response)

    # Try attribute-style access from response objects
    answer_attr = getattr(response, 'response', None)
    if answer_attr:
        return answer_attr

    return str(response)