import os
import requests

BOT_TOKEN = os.getenv("7794145234:AAGTiTtmppgfHfMZk4atX6KR9gO7c2Vaoxg")
TELEGRAM_USER_ID = os.getenv("5410947715")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": 5410947715,
        "text": message
    }
    requests.post(url, json=payload)
