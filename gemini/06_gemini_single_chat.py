import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

def ask_gemini(prompt):
    body = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    response = requests.post(URL, json=body)
    response.raise_for_status()

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]

user_input = input("Ask Gemini: ")
reply = ask_gemini(user_input)
print("\nGemini:", reply)
