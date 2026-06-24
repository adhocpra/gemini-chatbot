from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def ask_gemini(prompt):
    body = {"contents": [{"parts": [{"text": prompt}]}]}
    for attempt in range(3):
        response = requests.post(URL, json=body)
        if response.status_code in (429, 503):
            time.sleep(2 ** attempt)
            continue
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    response.raise_for_status()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=FileResponse)
def home():
    return "static/index.html"

@app.get("/health")
def root():
    return {"status": "ok"}

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
