import requests
from bs4 import BeautifulSoup

links = []

url = "http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
page = requests.get(url)
if page.ok:

    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.findAll("article", class_="product_pod")
    tables = soup.findAll('table', {'class': 'table table-striped'})
"""
    for product in products:
        a = product.find('a')
        link = a['href'].replace("../../..", "")
        links.append("http://books.toscrape.com/catalogue" + link)

url = "http://books.toscrape.com/catalogue/category/books/fantasy_19/page-2.html"
page = requests.get(url)
if page.ok:

    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.findAll("article", class_="product_pod")

    for product in products:
        a = product.find('a')
        link = a['href'].replace("../../..", "")
        links.append("http://books.toscrape.com/catalogue" + link)
        print(links)
        
with open('urls.csv', 'w') as file:
    for link in links:
        file.write(link + '\n')

with open('urls.csv', 'r') as file:
    for row in file:
        print(row)
"""

url = 'http://books.toscrape.com/catalogue/every-heart-a-doorway-every-heart-a-doorway-1_465/index.html'

response = requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    UPC = soup.find('table', {'class': 'table table-striped'}).find('td', {})
