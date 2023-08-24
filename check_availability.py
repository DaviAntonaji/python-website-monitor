import requests
import time
from datetime import datetime
from telegram import send_telegram_alert
from config import WEBSITE, MAX_ATTEMPTS
from messages import MESSAGE_WEBSITE_OFFLINE, MESSAGE_STATUS_CODE, MESSAGE_WEBSITE_DOWN

now = datetime.now()
timestamp = int(datetime.timestamp(now))
url = f"https://{WEBSITE}?v={timestamp}"


try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException:
    send_telegram_alert(WEBSITE, f"{MESSAGE_WEBSITE_OFFLINE}.")



for attempt in range(MAX_ATTEMPTS):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Website is up and running!")
            break
        else:
            raise Exception(f"{MESSAGE_STATUS_CODE} {response.status_code}")
    except Exception as e:
        if attempt == MAX_ATTEMPTS - 1:
            availability_alert_message = f"{MESSAGE_WEBSITE_DOWN} ({str(e)})"
            send_telegram_alert(WEBSITE, availability_alert_message)
            raise Exception(availability_alert_message)
        else:
            time.sleep(5)