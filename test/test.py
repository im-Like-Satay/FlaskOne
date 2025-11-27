from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("KEY_SECOND"),
    base_url="https://api.chatanywhere.tech/v1"
    # base_url="https://api.chatanywhere.org/v1"
)

completion = client.chat.completions.create(
    model="gpt-5.1-2025-11-13",
    messages = [
        {
            "role": "system",
            "content": "Kamu adalah seorang profesor bergelar PhD lulusan Oxford."
        },

        {
            "role": "user",
            "content": "1 + 1 = berapa?"
        },
    ],
    temperature=0.7,
)
print(completion.choices[0].message.content)