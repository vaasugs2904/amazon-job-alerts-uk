import os
import requests
import time
from datetime import datetime

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

AREAS = ["Luton", "Dunstable", "Hatfield"]

KEYWORDS = [
    "Amazon warehouse",
    "Amazon warehouse operative",
    "Amazon sortation",
    "Amazon fulfilment centre"
]

def send_alert(message):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("Set Telegram bot token and chat ID first.")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(
        url,
        data={"chat_id": CHAT_ID, "text": message},
        timeout=20
    )

def main():
    send_alert(
        "Amazon Job Alert bot started!\n"
        "Areas: Luton, Dunstable, Hatfield\n"
        "Job links: https://www.amazon.jobs/en/"
    )
    print("Bot started:", datetime.now())

if _name_ == "_main_":
    main()
