from urllib.parse import urlparse
import time
from datetime import datetime
from telegram import send_telegram_alert
from config import WEBSITE
from messages import MESSAGE_DNS_ERROR
import socket

url = f"https://{WEBSITE}"

parsed_url = urlparse(url)
domain = parsed_url.netloc
try:
    socket.gethostbyname(domain)
    print("DNS OK")
except socket.gaierror:
    send_telegram_alert(WEBSITE, MESSAGE_DNS_ERROR)
