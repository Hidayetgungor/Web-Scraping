import requests
from bs4 import BeautifulSoup

url = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar'

html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li",{"class":"column"})

for li in list:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    oldprice = li.find("div",{"class":"priceContainer"}).div.find_all("span")[0].text
    newprice = li.find("div",{"class":"priceContainer"}).div.find_all("span")[1].text
    print(f"name: {name} link: {link} oldprice: {oldprice} newprice: {newprice}")


