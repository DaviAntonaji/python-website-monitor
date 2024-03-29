import requests
import time
from datetime import datetime
from telegram import send_telegram_alert
from config import WEBSITE, MAX_RESPONSE_TIME
from messages import MESSAGE_SLOW_RESPONSE_TIME

now = datetime.now()
timestamp = int(datetime.timestamp(now))
url = f"https://{WEBSITE}?v={timestamp}"


start_time = time.time()
response = requests.get(url)
end_time = time.time()
response_time = end_time - start_time
print(f"Page loading time: {response_time:.2f} seconds")
if response_time > MAX_RESPONSE_TIME:
    slow_response_message = MESSAGE_SLOW_RESPONSE_TIME(response_time)
    send_telegram_alert(WEBSITE, slow_response_message)
    print(slow_response_message)
    raise Exception(slow_response_message)