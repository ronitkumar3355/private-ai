import requests
from config.api_keys import GOLD_API_KEY

def get_gold_price_inr():
    url = "https://www.goldapi.io/api/XAU/INR"
    headers = {
        "x-access-token": GOLD_API_KEY,
        "Content-Type": "application/json"
    }

    try:
        res = requests.get(url, headers=headers, timeout=10)
        data = res.json()

        price_per_ounce = data.get("price")
        if not price_per_ounce:
            return None

        # 1 troy ounce = 31.1035 grams
        price_per_gram = price_per_ounce / 31.1035
        return round(price_per_gram, 2)

    except Exception as e:
        return None