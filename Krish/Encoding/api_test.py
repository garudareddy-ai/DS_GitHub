import os
from openai import OpenAI
from dotenv import load_dotenv

# Load variables from your local .env file
load_dotenv()

# Initialize the OpenAI client pointing to GitHub's inference server
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ.get("GITHUB_TOKEN")
)

response = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful coding assistant."},
        {"role": "user", "content": "Write a python function to check if a number is prime."}
    ],
    model="gpt-4o-mini" # Or use "gpt-4o"
)

print(response.choices[0].message.content)