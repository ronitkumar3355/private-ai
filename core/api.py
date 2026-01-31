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

# Chat API
@app.post("/chat")
def chat(data: dict):
    user_input = data.get("message", "")
    reply = ask_ai(user_input)
    return {"reply": reply}

# UI serve
@app.get("/ui")
def serve_ui():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "frontend", "index.html")
    return FileResponse(file_path)