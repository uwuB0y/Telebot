import telebot
import requests
import time

token = "ur token"
chatid = "@channelUser"
bot = telebot.TeleBot(token)

def proxyGay(): 
    try:
        rq = requests.get("https://gimmeproxy.com/api/getProxy")
        protocol = rq.json()["protocol"]
        ipport = rq.json()["ipPort"]
        country = rq.json()["country"]
        messageProxy = f"*- New Proxy*\n*Ip-Port:* `{ipport}`.\n*Type:* {protocol}.\n*Country:* {country}.\n----- ------- ------- ----\n-=> [404](t.me/teamon404)"
        bot.send_message(chatid, messageProxy, parse_mode="markdown", disable_web_page_preview=True)
        print("done")
    except Exception as e:
        print(f"An error:\n{e}")
        return

def main():
    while True:
        proxyGay()
        time.sleep(300) #every 300sec

if __name__ == "__main__":
    main()