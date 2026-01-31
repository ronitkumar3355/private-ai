# core/safety.py

BANNED_KEYWORDS = [
    "hack", "crack", "steal", "ddos",
    "password break", "illegal", "fraud"
]

def is_safe(user_input: str) -> bool:
    text = user_input.lower()
    for word in BANNED_KEYWORDS:
        if word in text:
            return False
    return True