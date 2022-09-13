import requests, re
from discord_webhook import DiscordWebhook
from time import strftime
from time import localtime
from time import sleep
from bs4 import BeautifulSoup

#Initialize
gap = 3600
prevM = ""
date = strftime('%m/%d %H:%M', localtime())

while True:
    #Chapter 1: Getting Basic Information
    response = requests.get(
        "https://news.nknu.edu.tw/nknu_News/")
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find_all("td", limit = 3)[1]
    unit = str(soup.find_all("td", limit = 3)[2])[29:-5]
    rlist = str(result).split('>')
    website = "https://news.nknu.edu.tw/nknu_News/" + rlist[1][9:-17]
    temp = website.split("amp;")
    website = ''.join(x for x in temp)
    title = rlist[2][:-3]

    #Chapter 2: Consolidate Them
    response2 = requests.get(f"{website}")
    soup2 = BeautifulSoup(response2.text, "html.parser")
    desc = str(soup2.find_all('span')[5])[34:-15]
    desc = re.sub("[up\<\>\/]", '', desc).split("strong")

    dec = ''.join(x for x in desc if not "href" in x and x != "/p")
    finalM = f"最新公告! 公告處:{unit}\n☛{title}\n\n網站連結:{website}\n\n公告預覽:\n{dec}"
    #print(final_message)

    #Chapter 3: Send Into Oblivion
    if(finalM != prevM):
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1019106976409583707/dTM7dWoKUwljjDQKy7xptyk1EKZnVYeXbcEGr9hpUsmw9q_Y6LGegtJYBrQpqQnnTfhb', rate_limit_retry=True,
                             content=finalM)
        response = webhook.execute()
        prevM = finalM
    else:
        print("沒有更新...")

    print(f"目前時刻:{date}")

    #Chapter 4: And it repeats...

    sleep(gap)