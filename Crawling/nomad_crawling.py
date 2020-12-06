from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests


html = requests.get("https://nomadcoders.co/airbnb-clone")
soup = bs(html.text, "html.parser")
# pprint(html.text)

# mb4 = soup.findAll("div", {"class", "sc-AxhUy fxWvvr"})[4]

print(soup)