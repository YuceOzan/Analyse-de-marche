import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

all_books = []

links = []
final_links = []
categories = soup.findAll("ul", class_="nav nav-list")
for category in categories:
    hrefs = category.find_all('a', href=True)
    for href in hrefs:
        links.append(href['href'])
    for href in links:
        link_base = "http://books.toscrape.com/"
        full_link = link_base + href
        final_links.append(full_link)


books = []
for link in final_links:
    res = requests.get(link).text
    book_soup = BeautifulSoup(res, "html.parser")
    book_link = soup.find_all(class_="product_pod")
    for product in book_link:
        a = product.find('a')
        link = a['href'].replace("../../..", "")
        books.append("http://books.toscrape.com/" + link)

articles = []
for article in books:
    items = requests.get(article).text
    article_soup = BeautifulSoup(items, "html.parser")

    upc = article_soup.find(class_="table table-striped").td.text

    title = article_soup.find(class_="col-sm-6 product_main").h1.text
    price_with_tax = article_soup.find(class_="table table-striped").find_all('td')[3].text.replace('Â£', '')
    price_without_tax = article_soup.find(class_="table table-striped").find_all('td')[2].text.replace('Â£', '')
    available = article_soup.find(class_="table table-striped").find_all('td')[5].text.replace('In stock (', '')
    book_category = article_soup.find(class_="breadcrumb").find_all('a')[2].text
    image = article_soup.find(class_="item active").find('img')['src'].replace("../..", "http://books.toscrape.com")
    review = article_soup.find(class_="table table-striped").find('td').text[-1]
    description = article_soup.select("article.product_page > p")

    book = {"title": title, "price_including_tax": price_with_tax, "price_excluding_tax": price_without_tax,
            "number_available": available, "product_description": description, "category": book_category,
            "image_url": image, "review_rating": review}
    all_books.append(book)

print(all_books)






"""
        'title': soup.find('div', {'class', 'col-sm-6 product_main'}).find('h1').text,
        'price_with_tax': soup.find('table', {'class': 'table table-striped'}).find_all('td')[3].text.replace('Â', ''),
        'pricetax': soup.find('table', {'class': 'table table-striped'}).find_all('td')[2].text.replace('Â', ''),
        'available': soup.find('table', {'class': 'table table-striped'}).find_all('td')[5].text,
        'category': soup.find('ul', {'class', 'breadcrumb'}).find_all('a')[2].text,
        'review': soup.find('table', {'class', 'table table-striped'}).find('td').text[-1],
        'image': soup.find('div', {'class', 'item active'}).find('img')['src'].replace('../..', 'http://books.toscrape.com'),
        'description': soup.select("article.product_page > p"),






url2 = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
page = requests.get(url2)
soup2 = BeautifulSoup(page.content, 'html.parser')

books = []
book_links = soup2.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
for book_link in book_links:
    link2 = book_link.find("h3").a.get("href")
    link = link2.replace("../../..", "http://books.toscrape.com/catalogue")
    complete_link = link
    books.append(complete_link)
print(books)

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
