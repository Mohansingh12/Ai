from openai import OpenAI

openai = OpenAI(api_key="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")

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
    