from openai import OpenAI

def OpenAI():
    client = OpenAI(api_key="your-api-key")

    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "mention five words"}], max_tokens=10)
    print(response.choices[0].message.content)