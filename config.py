import os

WEBSITE = os.getenv("WEBSITE")
MAX_RESPONSE_TIME=int(os.getenv("MAX_RESPONSE_TIME"))
MAX_ATTEMPTS = int(os.getenv("MAX_ATTEMPTS"))
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")