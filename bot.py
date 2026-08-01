import time
import requests
from telegram import Bot

BOT_TOKEN = "8659833120:AAGOddhqecy2XXvCTgd0y-xZ7UriWvH4Pks"
CHANNEL = "@redix_mt"

STREAMERS = [
    "AbuSwe7l",
    "absi",
    "drb7h",
    "fwaz",
    "id7o",
    "SXB",
    "f1aisal",
    "sodry",
    "fhlwy",
    "seagull"
]

bot = Bot(BOT_TOKEN)

def is_live(username):
    try:
        url = f"https://kick.com/api/v2/channels/{username}"
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )

        if response.status_code != 200:
            return False, None

        data = response.json()
        livestream = data.get("livestream")

        if livestream:
            return True, livestream.get("session_title", "بدون عنوان")

        return False, None

    except Exception as e:
        print(e)
        return False, None


if __name__ == "__main__":
    print("🚀 Bot Started")

    sent = set()

    while True:
        for username in STREAMERS:
            live, title = is_live(username)

            if live and username not in sent:
                bot.send_message(
                    chat_id=CHANNEL,
                    text=f"🔴 بدأ بث جديد!\n\n👤 {username}\n📝 {title}\n\nhttps://kick.com/{username}"
                )
                sent.add(username)

            elif not live and username in sent:
                sent.remove(username)

        time.sleep(60)
