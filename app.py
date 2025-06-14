from flask import Flask, request
from trade_logic import get_trade_signal
from telegram import send_telegram_message
import os

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    best_trade = select_best_trade(data)
    if best_trade:
        send_telegram_message(best_trade)
    return {"status": "received"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
