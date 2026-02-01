from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from core.ai_brain import ask_ai

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Root (Render HEAD check ke liye)
@app.api_route("/", methods=["GET", "HEAD"])
def root():
    return {"status": "ok"}

# ✅ Health (Render check)
@app.api_route("/health", methods=["GET", "HEAD"])
def health():
    return {"status": "ok"}

# ✅ Chat API
@app.post("/chat")
def chat(data: dict):
    user_input = data.get("message", "")
    reply = ask_ai(user_input)
    return {"reply": reply}

# ✅ UI serve (frontend)
@app.get("/ui")
def serve_ui():
    return FileResponse("core/frontend/index.html")