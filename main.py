from flask import Flask
import os
import requests

app = Flask(__name__)

# Get bot credentials from Render environment variables
BOT_TOKEN = os.environ.get("7794145234:AAGTiTtmppgfHfMZk4atX6KR9gO7c2Vaoxg")
CHAT_ID = os.environ.get("5410947715")

@app.route('/')
def home():
    return "✅ Bot is live and running!"

@app.route('/send')
def send_message():
    if not BOT_TOKEN or not CHAT_ID:
        return "❌ Bot token or Chat ID not found in environment variables."

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": "📢 This is a test message from Render Flask bot!",
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        return f"✅ Message sent! Status: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"❌ Failed to send message: {e}"
