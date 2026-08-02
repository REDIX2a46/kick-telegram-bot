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

    # إرسال البثوث الموجودة وقت التشغيل
    for username in STREAMERS:
        live, title = is_live(username)

        if live:
            bot.send_message(
                chat_id=CHANNEL,
                text=f"🔴 بث موجود الآن!\n\n👤 {username}\n📝 {title}\n\nhttps://kick.com/{username}"
            )
            sent.add(username)


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
