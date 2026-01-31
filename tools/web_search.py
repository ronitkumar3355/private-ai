import requests

def web_search(query):
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

        results = []

        if data.get("AbstractText"):
            results.append(data["AbstractText"])

        for topic in data.get("RelatedTopics", [])[:3]:
            if isinstance(topic, dict) and topic.get("Text"):
                results.append(topic["Text"])

        if not results:
            return "No clear result found from internet."

        return " | ".join(results)

    except Exception as e:
        return f"Internet error: {e}"