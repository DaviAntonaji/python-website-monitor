import os
import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
def send_telegram_alert(msg):
    
    URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "text": msg,
        "chat_id": TELEGRAM_CHAT_ID
    }
    response = requests.post(URL, json=payload)
    if response.status_code != 200:
        raise Exception("Failed to send Telegram alert!")