from enum import Flag
from bs4.element import TemplateString
import requests, re
from discord_webhook import DiscordWebhook
from datetime import datetime
from time import strftime
from time import localtime
from bs4 import BeautifulSoup
#To optimize the texts
def optimize(s):
    flag = 0
    ret = ""
    for i in range(len(s)):
        if(s[i] == '<'): flag = 0
        if(flag): ret += s[i]
        if(s[i] == '>'): flag = 1
    return ret
#To optimize the URL
def get_website(s):
    cot = 0
    ret = ""
    for i in range(len(s)):
        if(cot == 4): break
        if(cot == 3): ret += s[i]
        if(s[i] == '"'): cot += 1
    temp = ret.split("amp;")
    ret = ''.join(x for x in temp)
    return ret[:-1]

#Initialize
now = datetime.now()
date = now.strftime('%Y.%m.%d')
#date = '2022.09.16' Just for test

#Chapter 1: Getting Basic Information
response = requests.get(
    "https://news.nknu.edu.tw/nknu_News/")
soup = BeautifulSoup(response.text, "html.parser")
listing = soup.find_all("td", limit = 90) #Get the whole page
info_ = [listing[x] for x in range(90) if x%6 == 1]
unit_ = [listing[x] for x in range(90) if x%6 == 2]
date_ = [listing[x] for x in range(90) if x%6 == 3]
p_info = [str(info_[y]) for y in range(len(date_)) if date in str(date_[y])]
p_unit = [optimize(str(unit_[y])) for y in range(len(date_)) if date in str(date_[y])]

p_website = ["https://news.nknu.edu.tw/nknu_News/" + get_website(z) for z in p_info]
p_title = [optimize(z) for z in p_info]

no_update = True if not p_info else False

#Chapter 2: Consolidate Them
f_group = [f"{date} | 最新公告! 公告處:{p_unit[w]}\n\n➤  {p_title[w]}\n\n➤  網站連結: {p_website[w]}\n----------------------------------------\n" for w in range(len(p_info))]

#Chapter 3: Send Into Oblivion
if(not no_update):
    for final in f_group:
        #print(final) For debugging
        webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/1019081282002632744/aOhQ3FBys64iqsO85c1n4yw8cwSgA5Kl7LWb4qR6jSG6Gk82O-h2djkVnNPDrXHOAi7z', rate_limit_retry=True,content=final)
        response = webhook.execute()
    print("發現更新，已推播至DC伺服器!")
else:
    print("沒有更新...")

print(f"程式執行完畢，目前時刻:{date}")

#Chapter 4: And it repeats...

#Program by Bernie