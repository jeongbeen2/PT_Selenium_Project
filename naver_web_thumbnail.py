from bs4 import BeautifulSoup
from pprint import pprint
import requests, re
from urllib.request import urlretrieve

html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, "html.parser")
html.close()

data1_list = soup.findAll("div", {"class": "col_inner"})

li_list = []
for data1 in data1_list:
    li_list.extend(data1.findAll("li"))

for li in li_list:
    img = li.find("img")
    title = img["title"]
    img_src = img["src"]
    title = re.sub("[^0-9a-zA-Zㄱ-힗]", "", title)
    print(title, img_src)
    urlretrieve(img_src, title + ".")