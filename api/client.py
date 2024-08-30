import requests

def ping(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # Assuming the URL returns JSON
        else:
            return {"error": "Ping failed", "status_code": response.status_code}
    except requests.RequestException as e:
        return {"error": str(e)}

# from openai import OpenAI
# def OpenAI():
#     client = OpenAI(api_key="your-api-key")

#     response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "mention five words"}], max_tokens=10)
#     print(response.choices[0].message.content)