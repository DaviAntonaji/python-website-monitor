import requests
import time
from datetime import datetime
from telegram import send_telegram_alert
from config import WEBSITE
from bs4 import BeautifulSoup
from messages import MESSAGE_LINK_COULDNT_BE_VERIFIED, MESSAGE_BROKEN_LINK_FOUND

now = datetime.now()
timestamp = int(datetime.timestamp(now))
url = f"https://{WEBSITE}?v={timestamp}"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

healthy = True
for link in soup.find_all("a", href=True):
    link_url = link["href"]
    # Linkedin block requests for python
    if link_url.startswith("http") and "linkedin" not in link_url:
        try:
            print("Verifying", link_url)
            link_response = requests.head(link_url)
            if link_response.status_code >= 400:
                healthy = False
                send_telegram_alert(WEBSITE, f"{MESSAGE_BROKEN_LINK_FOUND}: {link_url}")
        except requests.exceptions.RequestException as e:
            healthy = False
            send_telegram_alert(WEBSITE, f"{MESSAGE_LINK_COULDNT_BE_VERIFIED} {link_url}")

if not healthy:
    raise Exception("Broken links founded")