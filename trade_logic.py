import pandas as pd
from utils import calculate_ema, is_pivot_breakout, check_volume_surge, check_momentum

def get_trade_signal():
    # Load stock data (example: from CSV or API)
    df = pd.read_csv("data/reliance_2025-04-01.csv")  # Replace with your input mechanism

    if is_pivot_breakout(df) and check_volume_surge(df) and check_momentum(df):
        entry_price = df.iloc[-1]["close"]
        stop_loss = entry_price * 0.98  # 2% SL
        target = entry_price * 1.02     # 2% target

        return (
            f"📈 *Breakout Alert (Scenario A)*\n"
            f"Stock: RELIANCE\n"
            f"Entry: ₹{entry_price:.2f}\n"
            f"Target: ₹{target:.2f}\n"
            f"Stop Loss: ₹{stop_loss:.2f}\n"
            f"Exit: Intraday or Target/SL Hit\n"
        )
    else:
        return None
