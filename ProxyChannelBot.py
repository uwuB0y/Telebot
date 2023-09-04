import telebot, time, requests, os

token = "TOKEN"  # bot token
chatid = "@urUserChannel"
chatidd = "userChannel without @"
delay = 10 # Delay between each message
bot = telebot.TeleBot(token)
while True: 
    try:
        rq = requests.get("https://gimmeproxy.com/api/getProxy") # get a random proxy
        protocol = rq.json()["protocol"]
        ipport = rq.json()["ipPort"]
        speed = rq.json()["speed"]
        country = rq.json()["country"]
        messageProxy = f"*- New Proxy*\n*Ip-Port:* `{ipport}`.\n*Type:* {protocol}.\n*Speed:* {speed}\n*Country:* {country}\n----- ------- ------- ----\n=> [Follow us](t.me/{chatidd})"
        bot.send_message(chatid, messageProxy, parse_mode="markdown", disable_web_page_preview=True) # Send the message
        time.sleep(delay) # Delay
    except Exception as e:
        print(e)
