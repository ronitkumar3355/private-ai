import requests
from datetime import datetime

def check_news_freshness(query):
    url = "https://api.duckduckgo.com/"
    params = {
        "q": query,
        "format": "json",
        "no_redirect": 1,
        "no_html": 1
    }

    try:
        res = requests.get(url, params=params, timeout=10)
        data = res.json()

        if data.get("AbstractText"):
            return f"📰 Latest info: {data['AbstractText']}"

        for topic in data.get("RelatedTopics", []):
            if isinstance(topic, dict) and topic.get("Text"):
                return f"📰 Possible update: {topic['Text']}"

        return "⚠️ Is topic par koi *recent / confirmed news* nahi mili."

    except Exception as e:
        return f"❌ News fetch error: {e}"