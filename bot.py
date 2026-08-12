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
        url = "https://kick.com/api/graphql"

        payload = {
            "operationName": "Channel",
            "variables": {
                "slug": username
            },
            "query": """
            query Channel($slug: String!) {
              channel(slug: $slug) {
                livestream {
                  isLive
                  session_title
                }
              }
            }
            """
        }

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        r = requests.post(url, json=payload, headers=headers, timeout=10)

        print(r.status_code)
        print(r.text[:500])

        if r.status_code != 200:
            return False, None

        data = r.json()

        livestream = data.get("data", {}).get("channel", {}).get("livestream")

        if livestream and livestream.get("isLive"):
            return True, livestream.get("session_title", "بث مباشر")

        return False, None

    except Exception as e:
        print(e)
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
