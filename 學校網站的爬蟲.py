import requests, re
from bs4 import BeautifulSoup

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
final_message = f"最新公告! 公告處:{unit}\n{title}\n網站連結:{website}\n\n公告預覽(可能會有點奇怪):\n{dec}"
#print(final_message)

#Chapter 3: Send Into Oblivion
evt = "info_updated"
key = "bgSBNfTuWeTf0X1eoSCPMi"
val = final_message
url = (f'https://maker.ifttt.com/trigger/{evt}' + f'/with/key/{key}?value1=' + val)
r = requests.get(url)
print(r.text)
#print("Website: " + website + '\n' + "Title: " + title)