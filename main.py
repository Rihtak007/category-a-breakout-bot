from flask import Flask
import os
import requests

app = Flask(__name__)

# Get Telegram credentials from environment
BOT_TOKEN = os.environ.get("7794145234:AAGTiTtmppgfHfMZk4atX6KR9gO7c2Vaoxg")
CHAT_ID = os.environ.get("5410947715")

@app.route('/')
def home():
    return "✅ Flask bot is live!"

@app.route('/send')
def send():
    if not BOT_TOKEN or not CHAT_ID:
        return "❌ BOT_TOKEN or CHAT_ID not set."

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": "📈 This is a test message from your bot!",
        "parse_mode": "Markdown"
    }

    try:
        r = requests.post(url, data=payload)
        r.raise_for_status()
        return f"✅ Message sent! Status: {r.status_code}"
    except Exception as e:
        return f"❌ Failed to send message: {str(e)}"

# Don't include if using gunicorn in Render
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=10000)
