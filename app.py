from flask import Flask, request
from trade_logic import select_best_trade
from utils import send_telegram_message

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    best_trade = select_best_trade(data)
    if best_trade:
        send_telegram_message(best_trade)
    return {"status": "received"}, 200