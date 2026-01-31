# core/auth.py

OWNER_PASSWORD = "1234"  # abhi simple, baad me secure karenge

def check_auth():
    pwd = input("🔐 Enter password: ")
    if pwd != OWNER_PASSWORD:
        print("❌ Access denied")
        return False
    print("✅ Access granted")
    return True