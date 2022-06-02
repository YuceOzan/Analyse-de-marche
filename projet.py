import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

books = []

links = []

categories = soup.findAll("ul", class_="nav nav-list")

for category in categories:
    category_link = category.find('li').a.get('href')
    link_base = "http://books.toscrape.com/"
    full_link = link_base + category_link
    print(full_link)

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


url = 'http://books.toscrape.com/catalogue/unicorn-tracks_951/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


livre = {
        'upc': soup.find('table', {'class': 'table table-striped'}).find_all('td')[0].text,
        'title': soup.find('div', {'class', 'col-sm-6 product_main'}).find('h1').text,
        'price_with_tax': soup.find('table', {'class': 'table table-striped'}).find_all('td')[3].text.replace('Â', ''),
        'pricetax': soup.find('table', {'class': 'table table-striped'}).find_all('td')[2].text.replace('Â', ''),
        'available': soup.find('table', {'class': 'table table-striped'}).find_all('td')[5].text,
        'category': soup.find('ul', {'class', 'breadcrumb'}).find_all('a')[2].text,
        'review': soup.find('table', {'class', 'table table-striped'}).find('td').text[-1],
        'image': soup.find('div', {'class', 'item active'}).find('img')['src'].replace('../..', 'http://books.toscrape.com'),
        'description': soup.select("article.product_page > p"),
    }
print(livre)
"""
