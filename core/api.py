from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from core.ai_brain import ask_ai
import os

app = FastAPI()

# CORS (frontend se call ke liye)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root check
@app.get("/")
def home():
    return {"status": "Private AI is running 🚀"}

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}

# Chat API
@app.post("/chat")
def chat(data: dict):
    user_input = data.get("message", "")
    reply = ask_ai(user_input)
    return {"reply": reply}

# UI serve
@app.get("/ui")
def serve_ui():
    return FileResponse("core/frontend/index.html")