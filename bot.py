import os
import time
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("Telegram bot token is missing")

API = f"https://api.telegram.org/bot{TOKEN}"

def send_message(chat_id, text):
    requests.post(
        f"{API}/sendMessage",
        json={"chat_id": chat_id, "text": text},
        timeout=20
    ).raise_for_status()

def main():
    offset = None
    print("Amazon Jobs Telegram bot is running")

    while True:
        try:
            response = requests.get(
                f"{API}/getUpdates",
                params={"offset": offset, "timeout": 25},
                timeout=35
            )
            response.raise_for_status()

            for update in response.json().get("result", []):
                offset = update["update_id"] + 1
                message = update.get("message", {})
                chat_id = message.get("chat", {}).get("id")
                command = message.get("text", "").strip().lower()

                if not chat_id:
                    continue

                if command in ("/start", "/help"):
                    send_message(
                        chat_id,
                        "Welcome to Amazon UK Job Alerts!\n\n"
                        "Send jobs to get Amazon job links.\n"
                        "Areas: Luton, Dunstable and Hatfield."
                    )
                elif command == "jobs" or command == "/jobs":
                    send_message(
                        chat_id,
                        "Amazon Jobs UK:\n"
                        "https://www.amazon.jobs/en/\n\n"
                        "Search warehouse roles near Luton, "
                        "Dunstable and Hatfield."
                    )
                else:
                    send_message(
                        chat_id,
                        "Mowa! Send /start or type jobs "
                        "to get Amazon job links."
                    )

        except Exception as error:
            print("Error:", error)
            time.sleep(5)

if __name__ == "__main__":
    main()
