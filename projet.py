import requests
from bs4 import BeautifulSoup

links = []

for i in range(4):
    print(i)

url = "http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
page = requests.get(url)
if page.ok:

    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.findAll("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    for product in products:
        a = product.find('a')
        link = a['href']
        linkFull = link.replace("../../..", "")
        links.append("http://books.toscrape.com/catalogue" + linkFull)

    print(links)