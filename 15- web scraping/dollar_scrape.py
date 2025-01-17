import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.tgju.org/profile/price_dollar_rl")

soup = BeautifulSoup(res.text, "html.parser")

print(soup.find("span", attrs={"data-col": "info.last_trade.PDrCotVal"}).text)
