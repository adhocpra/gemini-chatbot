import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

history = []

def chat(user_message):
    history.append({
        "role": "user",
        "parts": [{"text": user_message}]
    })

    body = {"contents": history}

    response = requests.post(URL, json=body)
    response.raise_for_status()

    reply = response.json()["candidates"][0]["content"]["parts"][0]["text"]

    history.append({
        "role": "model",
        "parts": [{"text": reply}]
    })

    return reply


print("Gemini Chatbot — type 'quit' to exit")
print("-" * 40)

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    reply = chat(user_input)
    print(f"Gemini: {reply}\n")
