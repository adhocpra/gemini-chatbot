from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

def ask_gemini(prompt):
    body = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(URL, json=body)
    response.raise_for_status()
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello world"}

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    reply = ask_gemini(req.message)
    return {"reply": reply}

@app.get("/greet/{name}")
def greet(name: str):
    return {"greeting": f"Hello {name}!"}

messages = []

@app.post("/messages")
def add_message(req: ChatRequest):
    messages.append(req.message)
    return {"stored": req.message, "total": len(messages)}

@app.get("/messages")
def get_messages():
    return {"messages": messages}

@app.delete("/messages")
def delete_messages():
    messages.clear()
    return {"status": "all messages deleted"}
