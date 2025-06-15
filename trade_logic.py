import pandas as pd
import yfinance as yf
from utils import is_pivot_breakout, check_volume_surge, check_momentum

def get_trade_signal():
    try:
        stocks_df = pd.read_csv("stocks_list.csv")
    except FileNotFoundError:
        return "❌ stocks_list.csv not found."

    best_trade = None

    for symbol in stocks_df["Symbol"]:
        yahoo_symbol = symbol + ".NS"  # NSE format for Yahoo Finance
        data = yf.download(yahoo_symbol, period="15d", interval="1d", progress=False)

        if data.empty or len(data) < 2:
            continue

        df = data.reset_index()
        df.rename(columns={
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume"
        }, inplace=True)

        if is_pivot_breakout(df) and check_volume_surge(df) and check_momentum(df):
            entry_price = round(df.iloc[-1]["close"], 2)
            sl = round(entry_price * 0.99, 2)
            target = round(entry_price * 1.02, 2)

            best_trade = f"""📈 *Category A Breakout Trade (Scenario A)*
Stock: {symbol}
Entry: ₹{entry_price}
Target: ₹{target}
Stop Loss: ₹{sl}
Risk-Reward: 1:2
Exit: Intraday or T/SL Hit
"""
            break

    return best_trade or "❌ No valid breakout setup found in stocks list."
