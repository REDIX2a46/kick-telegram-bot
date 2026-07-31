def is_live(username):
    try:
        url = f"https://kick.com/api/v2/channels/{username}"

        r = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10,
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


if __name__ == "__main__":

    if not BOT_TOKEN:
        raise ValueError("لم يتم العثور على BOT_TOKEN في Environment Variables")

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
                        ),
                    )

                    sent.add(username)

                elif not live and username in sent:
                    sent.remove(username)

            time.sleep(60)

        except Exception as e:
            print(f"خطأ: {e}")
            time.sleep(10)
