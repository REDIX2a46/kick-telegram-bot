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

bot = telebot.TeleBot(BOT_TOKEN)

sent = set()


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

        if data.get("livestream"):
            return True, data["livestream"].get(
                "session_title",
                "بدون عنوان"
            )

        return False, None

    except Exception as e:
        print(e)
        return False, None


print("🚀 Bot Started")

bot.send_message(
    CHANNEL,
    "أخيراً ضبط البوت الحمد لله 🤩"
)


# إرسال البثوث الموجودة وقت تشغيل البوت
for username in STREAMERS:
    live, title = is_live(username)

    if live:
        keyboard = types.InlineKeyboardMarkup()

        button = types.InlineKeyboardButton(
            "مـشـاهـده مـمـتـعـه 🤩",
            url=f"https://kick.com/{username}"
        )

        keyboard.add(button)

        bot.send_message(
            CHANNEL,
            f"🔴 بث مباشر الآن!\n\n"
            f"👤 {username}\n"
            f"📝 {title}",
            reply_markup=keyboard
        )

        sent.add(username)


while True:

    for username in STREAMERS:

        live, title = is_live(username)

        if live and username not in sent:

            keyboard = types.InlineKeyboardMarkup()

            button = types.InlineKeyboardButton(
                "مـشـاهـده مـمـتـعـه 🤩",
                url=f"https://kick.com/{username}"
            )

            keyboard.add(button)

            bot.send_message(
                CHANNEL,
                f"🔴 بدأ بث جديد!\n\n"
                f"👤 {username}\n"
                f"📝 {title}",
                reply_markup=keyboard
            )

            sent.add(username)

        elif not live and username in sent:
            sent.remove(username)

    time.sleep(60)
