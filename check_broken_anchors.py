import requests
import time
from datetime import datetime
from telegram import send_telegram_alert
from config import WEBSITE
from bs4 import BeautifulSoup


now = datetime.now()
timestamp = int(datetime.timestamp(now))
url = f"https://{WEBSITE}?v={timestamp}"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


for link in soup.find_all("a", href=True):
    link_url = link["href"]
    print("Verifying", link_url)
    if not link_url.startswith("http"):
        continue
    try:
        link_response = requests.head(link_url)
        if link_response.status_code >= 400:
            send_telegram_alert(f"{WEBSITE} Broken link found: {link_url}")
    except requests.exceptions.RequestException:
        send_telegram_alert(f"{WEBSITE} The link couldn't be verified: {link_url}")
