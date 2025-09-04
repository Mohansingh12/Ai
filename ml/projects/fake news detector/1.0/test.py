from openai import OpenAI

# Initialize client with your API key
client = OpenAI(api_key="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")

def detect_fake_news(text):
    prompt = f"""
    You are a fake news detector AI. 
    Classify the following news as either REAL or FAKE.
    Also give a short explanation why you think so.

    News: "{text}"
    """
    
    response = client.chat.completions.create(
        model="",  # fast & cheap model
        messages=[{"role": "user", "content": prompt}],
        temperature=0  # more deterministic
    )
    
    return response.choices[0].message.content

# Test
news = "Breaking: Aliens have landed in New York City!"
print(detect_fake_news(news))
