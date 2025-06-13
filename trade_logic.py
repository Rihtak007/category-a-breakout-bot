def select_best_trade(data):
    ticker = data.get("ticker")
    price = float(data.get("price"))
    volume = float(data.get("volume"))
    avg_volume = float(data.get("avg_volume", 0))
    rsi = float(data.get("rsi", 0))
    price_above_20ema = data.get("price_above_20ema", False)
    price_above_50ema = data.get("price_above_50ema", False)
    is_breaking_pivot = data.get("is_breaking_pivot", False)
    macd_crossover = data.get("macd_crossover", False)

    if (
        is_breaking_pivot and
        price_above_20ema and
        price_above_50ema and
        (volume > 1.5 * avg_volume) and
        (rsi > 55 or macd_crossover)
    ):
        entry = round(price, 2)
        target1 = round(entry * 1.015, 2)
        target2 = round(entry * 1.03, 2)
        target3 = round(entry * 1.05, 2)
        stop_loss = round(entry * 0.985, 2)

        return f"""[PRE-MARKET BREAKOUT ALERT]
Stock: {ticker}
Entry: Rs. {entry}
Target 1: Rs. {target1}
Target 2: Rs. {target2}
Target 3: Rs. {target3}
Stop Loss: Rs. {stop_loss}
Exit: 3:15 PM if no SL/Target hit
#Breakout #CategoryA #Intraday
""" 
    return None