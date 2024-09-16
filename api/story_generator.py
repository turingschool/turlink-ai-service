# you can add the OpenAI API key to your environmental variables so that you don’t add it directly to the Python file:
# use this => `export OPENAI_KEY="your-api-key"`

import os
from openai import OpenAI
client = OpenAI(api_key=os.environ["OPENAI_KEY"])
def generate_story(words):
    # Call the OpenAI API to generate the story
    response = get_short_story(words)
    # Format and return the response
    return format_response(response)

def get_short_story(body):
    # Construct the system prompt
    system_prompt = f"""You are a helpful assistant.
    Summarize the following content: {body}.
    Use 3 bullet points."""
    # Make the API call
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": system_prompt
        }],
        temperature=0.8,
        max_tokens=100
    )

    # Return the API response
    return response

def format_response(response):
    # Extract the generated story from the response
    story = response.choices[0].message.content
    # Remove any unwanted text or formatting
    story = story.strip()
    # Return the formatted story
    return story