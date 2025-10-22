import time
import requests
from acd_strategy import get_acd_signal, client, SYMBOL, INTERVAL

TELEGRAM_BOT_TOKEN = "8450884144:AAF-7prle9dtqtj8ftU4vKZNZ0h6n2XkWyI"
TELEGRAM_CHAT_ID = "6222023451"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id":TELEGRAM_CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"⚠ Telegram Error:{e}")

        if __name__ == "__main__":
             print("✅ACD Live Bot started. Monitoring market...")

        last_singal = None

        while True:
            try:
                signal = get_acd_signal(client, SYMBOL, INTERVAL)
                print(f"🔁 Checked: {SYMBOL} - Signal: {signal}")

                if signal and signal !=last_singal:

                    send_telegram(f"🚨 New ACD Signnal: {signal}")
                    print(f"✅ Alert sent: {signal}")
                    last_singal = signal
                else:
                    print("No new signal yet.")
            except Exception as e:
                print(f"⚠ Error: {e}")
time.sleep(300)

import time
import requests
from acd_strategy import get_acd_signal, client, SYMBOL, INTERVAL

TELEGRAM_BOT_TOKEN = "8450884144:AAF-7prle9dtqtj8ftU4vKZNZ0h6n2XkWyI"
TELEGRAM_CHAT_ID = "6222023451"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id":TELEGRAM_CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"⚠ Telegram Error:{e}")

        if __name__ == "__main__":
             print("✅ACD Live Bot started. Monitoring market...")
             print("✅ Bot started successfully and now running 24/7...")

             last_signal = None
        while True:
            try:
                signal = get_acd_signal(client, SYMBOL, INTERVAL)
                print(f"🔁 Checked: {SYMBOL} - Signal: {signal}")

                if signal and signal !=last_singal:

                    send_telegram(f"🚨 New ACD Signnal: {signal}")
                    print(f"✅ Alert sent: {signal}")
                    last_singal = signal
                else:
                    print("No new signal yet.")
                    while True:
                        try:
                            signal = get_acd_signal(client, SYMBOL, INTERVAL)
                            if signal == "BUY" and signal != last_signal:
                                send_telegram(f"✅ BUY Signal: Price crossed A-level for {SYMBOL}")
                                print(f"✅ BUY Signal sent for {SYMBOL}")
                                last_signal = signal
                            elif signal == "SELL" and signal != last_signal:
                                send_telegram(f"🔻 SELL Signal: Price fell below C-level for {SYMBOL}")
                                print(f"🔻 SELL Signal sent for {SYMBOL}")
                                last_signal = signal

                            else:
                                print(f"🔁 No new signal yet for {SYMBOL}")
                                
                                time.sleep(300)

            except Exception as e:
                print(f"⚠ Error: {e}")
                send_telegram(f"⚠ Error from bot: {e}")
                time.sleep(60)