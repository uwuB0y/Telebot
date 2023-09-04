import telebot, time, requests
bot = telebot.TeleBot("TOKEN")
while True: 
    try:
        rq = requests.get("https://gimmeproxy.com/api/getProxy") # get a random proxy
        bot.send_message(chatid, f"*- New Proxy*\n*Ip-Port:* `{rq.json()["ipPort"]}`.\n*Type:* {rq.json()["protocol"]}.\n*Speed:* {rq.json()["speed"]}\n*Country:* {rq.json()["country"]}\n----- ------- ------- ----\n=> [archlinux](t.me/linux_nerd)", parse_mode="markdown", disable_web_page_preview=True) # Send the message
        time.sleep(10) # Delay
    except:
        pass
