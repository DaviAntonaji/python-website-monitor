from datetime import datetime
import random
import json
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()


urls = os.getenv("URLS")
urls = urls.replace("'", '"')
urls = json.loads(urls)

max_erros = int(os.getenv("ERRORS_TO_ALERT"))
erros = 0
while True:
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    posicao = random.randint(0,len(urls)-1)
    url= urls[posicao] + "?v="+str(int(timestamp))

    try:
        response = requests.get(url)

        if response.status_code != 200:
            erros += 1
            if erros == max_erros:
                TOKEN = os.getenv("TELEGRAM_TOKEN")
                CHAT_ID= os.getenv("TELEGRAM_CHAT_ID")
                URL = "https://api.telegram.org/bot"+TOKEN+"/sendMessage"
                msg = os.getenv("ALERT_MESSAGE")
                obj = {
                    "text": msg,
                    "chat_id": CHAT_ID
                }
                x = requests.post(URL, data = obj)
                erros = 0
            else:
                print("Total de Erros: ", erros)
        else:
            erros = 0
            print("Everything is OK :)")
    except:
        erros += 1
        if erros == max_erros:
            TOKEN = os.getenv("TELEGRAM_TOKEN")
            CHAT_ID= os.getenv("TELEGRAM_CHAT_ID")
            URL = "https://api.telegram.org/bot"+TOKEN+"/sendMessage"
            msg = os.getenv("ALERT_MESSAGE")
            obj = {
                "text": msg,
                "chat_id": CHAT_ID
            }
            x = requests.post(URL, data = obj)

            erros = 0
        else:
            print("Total de Erros: ", erros)
    time.sleep(int(os.getenv("SLEEP_TIME_SECONDS")))