import os

# --- ENV VARIABLES ---
BOT_TOKEN = os.environ.get("7794145234:AAGTiTtmppgfHfMZk4atX6KR9gO7c2Vaoxg")
CHAT_ID = os.environ.get("5410947715")

def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, data=payload)
    return response.text

def format_trade_message(stock, entry, t1, t2, t3, sl, rr_ratio):
    return (
        f"🚀 *Breakout Alert* 🚀\n\n"
        f"*Stock:* {stock}\n"
        f"*Direction:* Long\n"
        f"*Entry:* ₹{entry}\n"
        f"*Target 1:* ₹{t1}\n"
        f"*Target 2:* ₹{t2}\n"
        f"*Target 3:* ₹{t3}\n"
        f"*Stop Loss:* ₹{sl}\n"
        f"*Risk:Reward:* {rr_ratio}\n"
        f"*Timeframe:* Intraday*\n"
        f"*Auto Exit:* 3:15 PM if no SL or target is hit"
    )

@app.route('/')
def home():
    return 'Bot is live!'

@app.route('/send')
def trigger_bot():
    best_trade = {
        "stock": "JUBLFOODS",
        "entry": 520,
        "t1": 530,
        "t2": 540,
        "t3": 555,
        "sl": 505,
        "rr": "1:2.5"
    }

    message = format_trade_message(
        best_trade["stock"],
        best_trade["entry"],
        best_trade["t1"],
        best_trade["t2"],
        best_trade["t3"],
        best_trade["sl"],
        best_trade["rr"]
    )
    result = send_telegram_message(message)
    return f"Message sent: {result}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
