import time
import requests
import telebot
from telebot import types

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
    "abdulrhman",
    "peerless",
    "isaedx",
    "abokyan",
    "reald8sh",
    "xkndrx",
    "zeus1i",
    "m7vb",
    "mshary_1",
    "nefoxd",
    "wolf",
    "firas",
    "imod",
    "z7lion",
    "1cjx"
]
sent = set()

bot = telebot.TeleBot(BOT_TOKEN)


def is_live(username):
    try:
        url = f"https://kick.com/{username}"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(url, headers=headers, timeout=10)

        if r.status_code != 200:
            print(f"{username} | HTTP {r.status_code}")
            return False, None

        text = r.text.lower()

        if '"livestream":{' in text or '"livestream": {' in text:
            return True, "بث مباشر"

        return False, None

    except Exception as e:
        print(f"{username} | {e}")
        return False, None
def send_notification(username, title):
    keyboard = types.InlineKeyboardMarkup()

    button = types.InlineKeyboardButton(
        "مـشـاهـده مـمـتـعـه 🤩",
        url=f"https://kick.com/{username}"
    )

    keyboard.add(button)

    bot.send_message(
        CHANNEL,
        f"{username} بدأ بث [{title}]\n\n"
        f"𝐊 𝐈 𝐂 𝐊 🟢𝐑 𝐄 𝐃 𝐈 𝐗 🟣",
        reply_markup=keyboard
    )
    print("🚀 Bot Started")

while True:
    for username in STREAMERS:
        live, title = is_live(username)

        print(f"{username} | live={live} | title={title}")

        if live and username not in sent:
            send_notification(username, title)
            sent.add(username)

        elif not live and username in sent:
            sent.remove(username)

    time.sleep(60)
