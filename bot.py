import requests
import time
from telegram import Bot

BOT_TOKEN = "8659833120:AAEuvKEL96xdU16bJ_Clh0ECD8vD4gkWzBg"

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
    "iabs",
    "drex-7a",
    "imonkey_d",
    "abo_khrbaa",
    "hook",
    "okb8",
    "abo8alyy",
    "moustache",
    "w1pey",
    "rayn",
    "osamah",
    "majah92",
    "s6mito",
    "brof2",
    "muvxn",
    "klo25",
    "s5b",
    "hamadsenpai",
    "ib6h",
    "islf",
    "morcei",
    "seagull",
    "i_sh7i",
    "drak0ola",
    "inq",
    "eagle",
    "1nex",
    "idew",
    "yznsa",
    "ysmo",
    "virus",
    "abunoo7",
    "abdulrhman"
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

        if r.status_code != 200:
            return False, None

        data = r.json()
        livestream = data.get("livestream")

        if livestream:
            title = livestream.get("session_title", "بدون عنوان")
            return True, title

        return False, None

    except Exception:
        return False, None


if name == "main":

    print("🚀 Kick Telegram Bot Started")

    sent = set()

    while True:
        try:
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

                elif not live and username in sent:
                    sent.remove(username)

            time.sleep(60)

        except Exception as e:
            print(f"خطأ: {e}")
            time.sleep(10)
