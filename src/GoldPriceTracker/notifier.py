import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_token = os.getenv("API_KEY")
user_id = os.getenv("USER_ID")

def notify(status):
    url = f"https://api.telegram.org/bot{api_token}/sendMessage"
    payload = {
        "chat_id": user_id,
        "text": "Price dropped, Check the current price update!",
        "parse_mode": "Markdown"
    }
    if status == 1:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        print("Message sent.")
        
    elif status == 0:
        payload["text"] = "Script refreshed. Prices will be tracked from today."
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        print("refreshed.")

    else:
        print("no price change.")
        pass