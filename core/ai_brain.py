import os
import requests
from datetime import datetime

from tools.web_search import web_search
from tools.gold_price import get_gold_price_inr
from tools.news_check import check_news_freshness

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv("OPENROUTER_API_KEY")

BLOCKED_WORDS = ["hack", "crack", "password", "illegal"]


def ask_ai(user_input):
    text = user_input.lower()

    # ❌ Illegal / harmful block
    for word in BLOCKED_WORDS:
        if word in text:
            return "❌ AI: Main illegal ya harmful cheez mein help nahi kar sakta."

    # 🟡 LIVE GOLD PRICE
    if ("gold" in text and "price" in text) or ("gold rate" in text):
        price = get_gold_price_inr()
        if price:
            return f"🟡 Aaj 24K gold ka live price approx ₹{price} per gram (India) hai."
        else:
            return "⚠️ Abhi gold ka live price fetch nahi ho pa raha."

    # 📰 NEWS
    if "news" in text or "khabar" in text or "breaking" in text:
        news = check_news_freshness(user_input)
        if news:
            return f"📰 Latest verified news:\n{news}"
        else:
            return "⚠️ Is topic par koi confirmed fresh news nahi mili."

    # 📅 Date
    if "aaj ka date" in text or "today date" in text:
        today = datetime.now().strftime("%d %B %Y")
        return f"🧠 AI: Aaj ki date {today} hai."

    # 🌐 Search
    if text.startswith("search "):
        query = user_input.replace("search ", "", 1)
        return f"🌐 AI: {web_search(query)}"

    # 🤖 LLM CALL
    if not API_KEY:
        return "❌ API key missing. Check OPENROUTER_API_KEY in environment."

    today = datetime.now().strftime("%d %B %Y")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://private-ai-wtp.onrender.com",
        "X-Title": "Private-AI",
    }

    data = {
        "model": "deepseek/deepseek-chat",
        "messages": [
            {
                "role": "system",
                "content": f"Aaj ki date {today} hai. User jis language me bole usi me reply karo."
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=25)
        result = response.json()

        print("OpenRouter Response:", result)  # Render logs

        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]

        return f"❌ OpenRouter Error: {result}"

    except Exception as e:
        return f"❌ Network Error: {e}"