import requests
import time
from datetime import datetime
from telegram import send_telegram_alert
from config import WEBSITE, MAX_ATTEMPTS

now = datetime.now()
timestamp = int(datetime.timestamp(now))
url = f"https://{WEBSITE}?v={timestamp}"



for attempt in range(MAX_ATTEMPTS):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Website is up and running!")
            break
        else:
            raise Exception(f"Status code != 200 [{response.status_code}]")
    except Exception as e:
        if attempt == MAX_ATTEMPTS - 1:
            availability_alert_message = f"[{WEBSITE}] Website is down ({str(e)})"
            send_telegram_alert(availability_alert_message)
            raise Exception(availability_alert_message)
        else:
            time.sleep(5)