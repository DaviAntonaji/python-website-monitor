from urllib.parse import urlparse
import time
from datetime import datetime
from telegram import send_telegram_alert
from config import WEBSITE
import socket

url = f"https://{WEBSITE}"

parsed_url = urlparse(url)
domain = parsed_url.netloc
try:
    socket.gethostbyname(domain)
    print("DNS OK")
except socket.gaierror:
    send_telegram_alert(f"{WEBSITE} The DNS domain is not configured correctly.")
