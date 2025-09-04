from openai import OpenAI

openai = OpenAI(api_key="YOUR_API_KEY")

model = "gpt-4o"    
temperature = 0.7
max_tokens = 1000

def fake_news_detector(article_text):
    response= openai.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": article_text
            }
        ],
        max_tokens=max_tokens,
        temperature=temperature
    )
    