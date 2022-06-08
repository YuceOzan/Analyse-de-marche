import requests
from bs4 import BeautifulSoup

project = []

url = 'http://books.toscrape.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

links = []
categories = soup.findAll("ul", class_="nav nav-list")
for category in categories:
    hrefs = category.find_all('a', href=True)
    for href in hrefs:
        links.append(href['href'])
new_links = [element.replace("catalogue", "http://books.toscrape.com/catalogue") for element in links]
del new_links[0]

page = 0
books = []


for link in new_links:
    r2 = requests.get(link).text
    book_soup = BeautifulSoup(r2, "html.parser")
    print("categorie: " + link)
    nextpage = True
    while nextpage:
        book_link = book_soup.find_all(class_="product_pod")
        for product in book_link:
            a = product.find('a')
            full_link = a['href'].replace("../../..", "")
            print("livre: " + full_link)
            books.append("http://books.toscrape.com/catalogue" + full_link)
        next_url = None
        if book_soup.find('li', class_='next') is None:
            nextpage = False
            page += 1
            print("pas de page suivante")
        else:
            next_url = book_soup.find(class_="next")
            print(next_url)
            r4 = requests.get(next_url).text
            book_soup = BeautifulSoup(r4, 'html.parser')
    #créer csv

"""
articles = []
for link in books:
    r3 = requests.get(link).text
    article_soup = BeautifulSoup(r3, "html.parser")

    upc = article_soup.find(class_="table table-striped").td.text
    title = article_soup.find(class_="col-sm-6 product_main").h1.text
    price_with_tax = article_soup.find(class_="table table-striped").find_all('td')[3].text.replace('Â£', '')
    price_without_tax = article_soup.find(class_="table table-striped").find_all('td')[2].text.replace('Â£', '')
    available = article_soup.find(class_="table table-striped").find_all('td')[5].text.replace('In stock (',
                                                                                               '').replace(')', '')
    book_category = article_soup.find(class_="breadcrumb").find_all('a')[2].text
    image = article_soup.find(class_="item active").find('img')['src'].replace("../..", "http://books.toscrape.com")
    description = article_soup.find(class_="product_page").find_all('p')[3].text.replace("â", '"') \
        .replace("â", '"').replace("â", "'").replace("â", "—").replace("â¢Â", "•").replace("Â", " ").replace(
        "â¢", "•")
    review = article_soup.find(class_="table table-striped").find('td').text[6]
    # review star is needed?

    book = {"title": title, "price_including_tax(£)": price_with_tax, "price_excluding_tax(£)": price_without_tax,
            "number_available": available, "product_description": description, "category": book_category,
            "image_url": image, "review_rating": review}
    project.append(book)
print(project)


with open('urls.csv', 'w') as file:
    for link in links:
        file.write(link + '\n')
with open('urls.csv', 'r') as file:
    for row in file:
        print(row)
url = 'http://books.toscrape.com/catalogue/unicorn-tracks_951/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

"""
