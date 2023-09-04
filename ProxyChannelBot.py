import telebot, time, requests
while True: 
    try:
        rq=requests.get("https://gimmeproxy.com/api/getProxy")
        telebot.TeleBot("TOKEN").send_message(chatid,f"*- New Proxy*\n*Ip-Port:* `{rq.json()["ipPort"]}`.\n*Type:* {rq.json()["protocol"]}.\n*Speed:* {rq.json()["speed"]}\n*Country:* {rq.json()["country"]}\n----- ------- ------- ----\n=> [archlinux](t.me/linux_nerd)",parse_mode="markdown",disable_web_page_preview=True)
        time.sleep(10)
    except:
        pass
