import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(res.text, "html.parser")

# print(soup.body.getText("hours"))
# print(soup.body.contents)
# print(soup.body.find_all("div"))
# print(soup.a)
# print(soup.find("div"))
