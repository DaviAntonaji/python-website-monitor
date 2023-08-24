import requests
import time
from datetime import datetime
from telegram import send_telegram_alert
from config import WEBSITE
from messages import MESSAGE_EXPECTED_CONTENT_NOT_FOUND

now = datetime.now()
timestamp = int(datetime.timestamp(now))
url = f"https://{WEBSITE}?v={timestamp}"

response = requests.get(url)

expected_content = "All Rights Reserved"
if expected_content not in response.text:
    send_telegram_alert(WEBSITE, MESSAGE_EXPECTED_CONTENT_NOT_FOUND)
    raise Exception(MESSAGE_EXPECTED_CONTENT_NOT_FOUND)
else:
    print("Expected content found on the page.")