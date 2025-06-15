import pandas as pd

def calculate_ema(df, period, column='close'):
    return df[column].ewm(span=period, adjust=False).mean()

def is_pivot_breakout(df):
    # Use last row and yesterday's high/low/close to calculate pivot
    if len(df) < 2:
        return False
    prev = df.iloc[-2]
    pivot = (prev['high'] + prev['low'] + prev['close']) / 3
    today_high = df.iloc[-1]['high']
    return today_high > pivot

def check_volume_surge(df, factor=1.5):
    # Compare latest volume with avg of last 10 volumes
    if len(df) < 11:
        return False
    avg_vol = df['volume'][-11:-1].mean()
    current_vol = df.iloc[-1]['volume']
    return current_vol > avg_vol * factor

def check_momentum(df):
    # Simple RSI-based momentum check
    if 'close' not in df or len(df) < 15:
        return False
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    last_rsi = rsi.iloc[-1]
    return last_rsi > 60
