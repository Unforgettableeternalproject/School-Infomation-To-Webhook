from bs4.element import TemplateString
import requests, re
from discord_webhook import DiscordWebhook
from datetime import datetime
from time import strftime
from time import localtime
from bs4 import BeautifulSoup

#Initialize
now = datetime.now()
date = now.strftime('%m/%d %H:%M')
f = open('previous.txt', 'r', encoding='UTF-8')
prevM = f.read()
#print(prevM)
w = open('previous.txt', 'w', encoding='UTF-8')

#Chapter 1: Getting Basic Information
response = requests.get(
    "https://news.nknu.edu.tw/nknu_News/")
soup = BeautifulSoup(response.text, "html.parser")
test = soup.find_all("td", limit = 90)
result = soup.find_all("td", limit = 3)[1]
unit = str(soup.find_all("td", limit = 3)[2])[29:-5]
rlist = str(result).split('>')
website = "https://news.nknu.edu.tw/nknu_News/" + rlist[1][9:-17]
temp = website.split("amp;")
website = ''.join(x for x in temp)
title = rlist[2][:-3]
print(test)
#Chapter 2: Consolidate Them
response2 = requests.get(f"{website}")
soup2 = BeautifulSoup(response2.text, "html.parser")
desc = str(soup2.find_all('span')[5])[34:-15]
desc = re.sub("[up\<\>\/]", '', desc).split("strong")

dec = ''.join(x for x in desc if not "href" in x and x != "/p")
finalM = f"最新公告! 公告處:{unit}\n->{title}\n\n網站連結:{website}\n\n公告預覽:\n{dec}"
#print(final_message)

#Chapter 3: Send Into Oblivion
if(title != prevM):
#    webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/1019106976409583707/dTM7dWoKUwljjDQKy7xptyk1EKZnVYeXbcEGr9hpUsmw9q_Y6LGegtJYBrQpqQnnTfhb', rate_limit_retry=True,
#                            content=finalM)
#    response = webhook.execute()
    print("發現更新，已推播至DC伺服器!")
else:
    print("沒有更新...")

w.write(title)
print(f"程式執行完畢，目前時刻:{date}")

#Chapter 4: And it repeats...

#Program by Bernie