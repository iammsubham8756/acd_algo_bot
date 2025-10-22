import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import requests
from datetime import datetime
from binance.client import Client
import time
import os

SYMBOL = "BTCUSDT"        
INTERVAL = "15m"  
LIMIT = 100
OR_MINUTES = 30
OFFSET_PERCENT = 0.2

print("✅ acd strategy file is running correctly")

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY") or "mhDCWMdClVucdu52sxHTwHUYhUn0srSLHmIMsgdiwsezUBYHzmOoIfkCTX3Hmlbk"
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET") or "PL2u7QeImZKZejLPohjUBNWQiqMjYWNegqkry6xaFiSJS91TLIGT2Aa3kFEaj9OV"

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)
client.TIME_OFFSET = client.get_server_time()['serverTime'] - int(time.time() * 1000)

candles = client.get_klines(symbol=SYMBOL, interval=INTERVAL, limit=LIMIT)
last_close = float(candles[-1][4])
print(f"✅ Latest BTCUSDT close price:{last_close}")

TELEGRAM_TOKEN = "8450884144:AAF-7prle9dtqtj8ftU4vKZNZ0h6n2XkWyI"
CHAT_ID = "6222023451"

def send_telegram(message):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("Telegram not configured.")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chart_id": CHAT_ID, "text":
            message}
    
    try:
        requests.post(url, data=data)
        print("✅ Telegram message sent successfully")
    except Exception as e:
        print("Telefram Error:", e)
        
    from binance import Client 
    client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)
    client.TIME_OFFSET = client.get_server_time()['serverTime'] - int(time.time() * 1000)

    try:
        account_info = client.get_account()
        print("✅ Binance connection successful")
    except Exception as e:
        print("❌ Binance connection failed:", e)
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Telegram Error:", e)

        def get_binance_data(symbol=SYMBOL, interval=INTERVAL, limit=LIMIT):
            url = "https://api.binance.com/api/v3/klines"
            params = {"symbol": symbol, "interval": interval, "limit": limit}
            response = requests.get(url, params=params)
            data = response.json()
            df = pd.DataFrame(data, columns=["time", "open", "high", "low", "close", "volume",
                                             "_1", "_2", "_3", "_4", "_5", "_6"
                                             ])
            df["time"] = pd.to_datetime(df["time"], unit="ms")
            df[["open", "high", "low", "close"]] = df[["open", "high", "low", "close"]].astype(float)
            return df
        
        def calculation_acd_levels(df):
            open_range = df.head(OR_MINUTES)
            or_high = open_range["high"].max()
            or_low = open_range["low"].min()
            low_mid = (or_high + or_low) / 2
            a_up = or_high + (or_high - or_low) * OFFSET_PERCENT
            c_down = or_low - (or_high - or_low) * OFFSET_PERCENT
            return or_high, or_low, a_up, c_down
        
def get_acd_signal(client, symbol, interval):
    try:
        klines = client.get_klines(symbol=symbol, interval=interval, limit=50)
        high = [float(k[2]) for k in klines]
        lows = [float(k[3]) for k in klines]
        closes = [float(k[4]) for k in klines]
        open_price = float(klines[0][1])
        high = max(high)
        low = min(lows)
        close = closes[-1]

        a_up = open_price + (high - low) *0.3
        a_down = open_price - (high -low)*0.3

        if close > a_up:
            return "BUY"
        elif close < a_down:
            return "SELL"
        else:
            return None
    except Exception as e:
        print(f"⚠ Error fetching ACD signal: {e}")
        return None

        def get_acd_strategy(df, or_high, or_low, a_up, c_down):
            plt.figure(figsize=(10,5))
            plt.plot(df['time'], df['close'], label="Close", color="blue")
            plt.axhline(or_high, color='green', linestyle="--", label="OR High")
            plt.axhline(or_low,color="red", linestyle="--", label="OR Low")
            plt.axhline(a_up, color="purple", linestyle="--", label="A Level (Buy Above)")
            plt.axhline(c_down, color="orange", linestyle="--", label="C Level (Sell Below)")
            plt.legend()
            plt.title("Mark B. Fisher ACD Levels")
            plt.xlabel("Time")
            plt.ylabel("Price")
            plt.show()

            if __name__ == "__main__":
                print("Fetching data from Binance...")
                df = get_binance_data()
                print("Calculating ACD levels...")
                or_high, or_low, or_mid, a_up, c_down = calculation_acd_levels(df)
                print(f"Opening Range Low: {or_low}")
                print(f"A Level: {a_up}")
                print(f"C Level: {c_down}")
                get_acd_strategy(df, or_high, or_low, a_up, c_down)

                last_close = df["close"].iloc[-1]
                if last_close > a_up:
                    send_telegram(f"🚀 BUY Signal! Price crossed A level: {last_close}")
                    print("BUY signal sent to Telegram.")
                elif last_close < c_down:
                    send_telegram(f"🔻 SELL Signal! Price fell below C Level: {last_close}")
                    print("SELL signal sent to Telegram.")
                else:
                    print("No trade signal currently.")

                    if __name__ == "__main__":
                        print("Fetching data from Binance...")
                        df = get_binance_data()
                        print("Calculating acd levels...")
                        a_up, a_down = calculation_acd_levels(df)
                        get_acd_strategy(df, a_up, a_down) 
                        send_telegram(f"✅ ACD Bot started! Latest BTCUSDT close: {df.iloc[-1]['close']}")