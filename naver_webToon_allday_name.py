from bs4 import BeautifulSoup
from pprint import pprint
import requests

html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, "html.parser")
html.close()

total_webToon_list = []
data1_list = soup.findAll("div", {"class": "col_inner"})
for data1 in data1_list:
    data2 = data1.findAll("a", {"class": "title"})
    data2_list = [t.text for t in data2]
    total_webToon_list.append(data2_list)
    # total_webToon_list.extend(data2_list)
pprint(total_webToon_list)