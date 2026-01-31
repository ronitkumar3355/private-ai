from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from core.ai_brain import ask_ai   # 🔥 REAL AI import

app = FastAPI()

# frontend serve
app.mount(
    "/static",
    StaticFiles(directory="core/frontend"),
    name="static"
)

@app.get("/")
def home():
    return FileResponse("core/frontend/index.html")

@app.post("/chat")
async def chat(data: dict):
    msg = data.get("message", "")
    reply = ask_ai(msg)   # 🔥 AI brain call
    return {"reply": reply}

@app.get("/health")
def health():
    return {"status": "ok"}