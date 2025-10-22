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

print("🚀 Sending test message to Telegram...")
send_telegram("🚀 Test message from ACD bot!")

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

print("🚀 Sending test message to Telegram...")
send_telegram("🚀 Test message from ACD bot!")
