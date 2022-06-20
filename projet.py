import requests
from bs4 import BeautifulSoup
import csv
url = 'http://books.toscrape.com'


def page(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def get_categorie(soup):
    links = []
    categories = soup.findAll("ul", class_="nav nav-list")
    for category in categories:
        hrefs = category.find_all('a', href=True)
        for href in hrefs:
            links.append(href['href'])
    new_categories = [element.replace("catalogue", "http://books.toscrape.com/catalogue") for element in links]
    del new_categories[0]
    return new_categories


def get_links(new_categories):
    books = []
    for link in new_categories:
        r2 = requests.get(link).text
        book_soup = BeautifulSoup(r2, "html.parser")
        print("categorie: " + link)
        nextpage = True
        while nextpage:
            book_link = book_soup.find_all(class_="product_pod")
            for product in book_link:
                a = product.find('a')
                full_link = a['href'].replace("../../..", "http://books.toscrape.com/catalogue")
                print("livre: " + full_link)
                books.append(full_link)
            if book_soup.find('li', class_='next') is None:
                nextpage = False
                print("pas de page suivante")
            else:
                next_page = book_soup.select_one('li.next>a').get('href')
                index = link.replace('/index.html', '')
                pg = next_page
                real_url = f"{index}/{pg}"
                print("Page suivante: " + real_url)
                r4 = requests.get(real_url).text
                book_soup = BeautifulSoup(r4, 'html.parser')
        with open("test.csv", 'w', newline='', encoding="utf-8") as csvfile:
            for book_url in books:
                r4 = requests.get(book_url).text
                book_url_soup = BeautifulSoup(r4, 'html.parser')
                book = get_book(book_url_soup)

                fieldnames = ["upc", "title", "price_including_taxes", 'price_excluding_tax', 'product_description', 'price_including_tax', 'number_available', 'image_url', 'category', 'review-rating']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(book)



    return books


def get_book(book_url_soup):
    upc = book_url_soup.find(class_="table table-striped").td.text
    # print(upc)
    title = book_url_soup.find(class_="col-sm-6 product_main").h1.text
    # print(title)
    price_with_tax = book_url_soup.find(class_="table table-striped").find_all('td')[3].text.replace('Â£', '')
    # print(price_with_tax)
    price_without_tax = book_url_soup.find(class_="table table-striped").find_all('td')[2].text.replace('Â£', '')
    # print(price_without_tax)
    available = book_url_soup.find(class_="table table-striped").find_all('td')[5].text.replace('In stock (',
                                                                                                '').replace(')', '')
    # print(available)
    book_category = book_url_soup.find(class_="breadcrumb").find_all('a')[2].text
    # print(book_category)
    image = book_url_soup.find(class_="item active").find('img')['src'].replace("../..", "http://books.toscrape.com")
    # print(image)
    image_download = requests.get(image).content
    description = book_url_soup.find(class_="product_page").find_all('p')[3].text.replace("â", '"') \
        .replace("â", '"').replace("â", "'").replace("â", "—").replace("â¢Â", "•").replace("Â", " ").replace(
        "â¢", "•").replace('â¦', "…").replace("Ã¢â¬", "").replace("Ã¢â¬", "").replace("Ã¢", "").replace("â", "–")
    # print(description)
    review = book_url_soup.find('p', class_='star-rating').get('class')[-1]
    # print(review)

    book = {"title": title, "upc": upc, "price_including_tax": price_with_tax,
            "price_excluding_tax": price_without_tax,
            "number_available": available, "product_description": description, "category": book_category,
            "image_url": image, "review-rating": review}

    return book


project = []

s = page(url)
l = get_categorie(s)
m = get_links(l)
o = get_book(m)
