# tools/internet.py

import requests

BLOCKED_WORDS = ["hack", "crack", "steal", "ddos"]

def search_web(query: str) -> str:
    q = query.lower()

    for word in BLOCKED_WORDS:
        if word in q:
            return "❌ Internet search blocked due to safety rules."

    url = "https://api.duckduckgo.com/"
    params = {
        "q": query,
        "format": "json",
        "no_redirect": 1,
        "no_html": 1
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        result = data.get("AbstractText")

        if result:
            return result
        else:
            return "ℹ️ No useful result found."
    except Exception as e:
        return f"⚠️ Internet error: {e}"