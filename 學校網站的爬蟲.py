import requests
from bs4 import BeautifulSoup
response = requests.get(
    "https://news.nknu.edu.tw/nknu_News/lastNewsList.aspx?cat=SCHOOLADMIN")
soup = BeautifulSoup(response.text, "html.parser")
result = soup.find_all("td", limit = 3)[1]
rlist = str(result).split('>')
website = "https://news.nknu.edu.tw/nknu_News/" + rlist[1][9:-17]
temp = website.split("amp;")
website = ''.join(x for x in temp)
title = rlist[2][:-3]

print("Website: " + website + '\n' + "Title: " + title)
#美化輸出環境
#架上伺服器(heroku?)
#每小時查詢最新消息有沒有變動
#整合進Discord Webhook