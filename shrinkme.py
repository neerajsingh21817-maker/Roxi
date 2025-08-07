import requests
from config import SHRINKME_API

def make_shortlink(original_url):
    url = "https://shrinkme.io/api"
    params = {
        "api": SHRINKME_API,
        "url": original_url
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if data["status"] == "success":
            return data["shortenedUrl"]
        else:
            print("❌ ShrinkMe response error:", data)
            return None
    except Exception as e:
        print("❌ ShrinkMe exception:", e)
        return None
