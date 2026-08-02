import time
import requests
from telegram import Bot

BOT_TOKEN = "8659833120:AAGiBwuyffp5en1YHXJBQiy35EXLJF9MDA0"
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
    "saad",
    "abo_khrbaa"
]

bot = Bot(BOT_TOKEN)


def is_live(username):
    try:
        url = f"https://kick.com/api/v2/channels/{username}"

        r = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )

        data = r.json()

        if data.get("livestream"):
            return True, data["livestream"].get(
                "session_title",
                "بدون عنوان"
            )

        return False, None

    except Exception as e:
        print(e)
        return False, None


if __name__ == "__main__":
    print("🚀 Bot Started")

    bot.send_message(
        chat_id=CHANNEL,
        text="✅ البوت اشتغل"
    )

    sent = set()

    while True:
        for username in STREAMERS:
            live, title = is_live(username)

            if live and username not in sent:
                bot.send_message(
                    chat_id=CHANNEL,
                    text=(
                        f"🔴 بدأ بث جديد!\n\n"
                        f"👤 {username}\n"
                        f"📝 {title}\n\n"
                        f"https://kick.com/{username}"
                    )
                )
                sent.add(username)

        time.sleep(60)
