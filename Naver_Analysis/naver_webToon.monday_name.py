from bs4 import BeautifulSoup
from pprint import pprint
import requests

html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, "html.parser")
html.close()

data1 = soup.find("div", {"class": "col_inner"})
# pprint(data1)
data2 = data1.findAll("a", {"class": "title"})
# pprint(data2)

# title_list = []
# for a in data2:
#     title_list.append(a.text)

title_list = [t.text for t in data2]
print(title_list)