from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get("https://search.naver.com/search.naver?query=날씨")
# pprint(html.text)

soup = bs(html.text, "html.parser")
# pprint(soup)

data1 = soup.find("div", {"class": "detail_box"})
pprint(data1)

data2 = data1.findAll("dd")
# pprint(data2)
good_day = data1.find("dd").text
good_day_slice = good_day[-2:]
# print(good_day_slice)

oh = data2[0].text
oh_slice = oh[-2:]
# print(oh_slice)

fine_dust = data2[0].find("span", {"class": "num"}).text
# print(fine_dust)

ultra_fine_dust = data2[1].find("span", {"class": "num"}).text
# print(ultra_fine_dust)

ozone = data2[2].find("span", {"class": "num"}).text

# print(ozone)
