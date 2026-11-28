import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

messages = [
    {
        "role": "system",
        "content": "Return only valid JSON. Do not include markdown."
    },
    {
        "role": "user",
        "content": """
        Create a fictional developer profile.
        Include name, age and skills.
        """
    }
]

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=messages,
    response_format={"type": "json_object"}
)

answer = response.choices[0].message.content

print("AI response:", answer)

data = json.loads(answer)

print("Name:", data["name"])
print("Age:", data["age"])
print("Skills:", data["skills"])

