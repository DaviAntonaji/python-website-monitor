import requests
import time
from datetime import datetime
from telegram import send_telegram_alert
from config import WEBSITE

now = datetime.now()
timestamp = int(datetime.timestamp(now))
url = f"https://{WEBSITE}?v={timestamp}"

response = requests.get(url)

expected_content = "All Rights Reserved"
if expected_content not in response.text:
    content_alert_message = f"{WEBSITE} Expected content not found on the page!"
    send_telegram_alert(content_alert_message)
    raise Exception(content_alert_message)
else:
    print("Expected content found on the page.")