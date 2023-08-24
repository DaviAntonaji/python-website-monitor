import requests
import time
from datetime import datetime
from telegram import send_telegram_alert
from config import WEBSITE
from bs4 import BeautifulSoup
from messages import MESSAGE_EMPTY_TITLE_TAG, MESSAGE_INVALID_TITLE_TAG


now = datetime.now()
timestamp = int(datetime.timestamp(now))
url = f"https://{WEBSITE}?v={timestamp}"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
title_tag = soup.find("title")
try:
    if title_tag:
        print("Verifying title...")
        title = title_tag.get_text()
        if not title:
            raise Exception(MESSAGE_EMPTY_TITLE_TAG)
        elif title != "Davi Antonaji":
            raise Exception(f"{MESSAGE_INVALID_TITLE_TAG} ({title})")

except Exception as e:
    send_telegram_alert(WEBSITE, str(e))
