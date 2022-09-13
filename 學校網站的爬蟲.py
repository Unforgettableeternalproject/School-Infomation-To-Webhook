import requests
from bs4 import BeautifulSoup
response = requests.get(
    "https://news.nknu.edu.tw/nknu_News/")
soup = BeautifulSoup(response.text, "html.parser")
result = soup.find_all("td", limit = 3)[1]
rlist = str(result).split('>')
website = "https://news.nknu.edu.tw/nknu_News/" + rlist[1][9:-17]
temp = website.split("amp;")
website = ''.join(x for x in temp)
title = rlist[2][:-3]

evt = "info_updated"
key = "bgSBNfTuWeTf0X1eoSCPMi"
val = title
url = (f'https://maker.ifttt.com/trigger/{evt}' + f'/with/key/{key}?value1={val}')
r = requests.get(url)
print(r.text)
print("Website: " + website + '\n' + "Title: " + title)
#���ƿ�X����
#�[�W���A��(heroku?)
#�C�p�ɬd�̷߳s�������S���ܰ�
#��X�iDiscord Webhook