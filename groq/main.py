from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
app=FastAPI()
client= Groq(api_key=os.getenv("GROQ_API_KEY"))

class Message(BaseModel):
    message: str
    history: list  =[]

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.post("/chat")
def chat(data: Message):
    messages= data.history + [{"role" : "user", "content" : data.message}]
    response= client.chat.completions.create(
        model= "llama-3.3-70b-versatile",
        messages= messages
    )
    return {"reply": response.choices[0].message.content}
app.mount("/static", StaticFiles(directory= "static"), name= "static")