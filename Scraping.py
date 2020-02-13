from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("http://books.toscrape.com/").text

soup = BeautifulSoup(source,'lxml')

# print(soup.prettify())

books = soup.find_all('article', class_="product_pod")
for book in books:
    title = book.h3.a.attrs['title']
    print(title)
    price = book.find('div', class_='product_price').p.text
    print(price)
    img_source = book.img.attrs['src']
    img_url = f'http://books.toscrape.com/{img_source}'
    print(img_url)



