import os
import requests

# Get OpenAI API key from environment variables
API_KEY = os.environ.get("OPENAI_KEY")
API_URL = "https://api.openai.com/v1/chat/completions"

def generate_story_from_openai(html_content):
  """
  Function that interacts with OpenAI API to generate a story summary
  based on the provided HTML content.
  """
  headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
  }

  data = {
    "model": "gpt-4o-mini",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": f"Summarize the following content: {html_content}."
      },
      {
        "role": "user",
        "content": "Use 3 numbered bullet points."
      }
    ]
  }

  try:
    # Make the POST request to OpenAI API
    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()

    # Return the story content from the OpenAI response
    openai_response = response.json()
    return openai_response['choices'][0]['message']['content'].strip()

  except requests.RequestException as e:
    raise Exception(f"OpenAI API request failed: {str(e)}")
  