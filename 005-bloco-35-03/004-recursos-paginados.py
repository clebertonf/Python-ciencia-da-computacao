from typing import Counter
import requests
from parsel import Selector

URL_BASE = 'http://books.toscrape.com/catalogue/'
NEXT_PAGE = 'page-1.html'

list_products = []
conunt = 0
while NEXT_PAGE:
    response = requests.get(URL_BASE + NEXT_PAGE)
    selector = Selector(text=response.text)

    titles = selector.css(".product_pod h3 a::attr(title)").getall()

    prices = selector.css(".product_price .price_color::text").getall()

    list_products.append(f"NAME: {titles[conunt]} PRICE: {prices[conunt]}")
    print(f"{len(list_products)} - {titles[conunt]}")
    print(list_products[conunt])

    conunt +=1
    if (conunt == 20):
        conunt = 0
        NEXT_PAGE = selector.css(".next a::attr(href)").get()
    
# Codigo percorre todas as paginas do site raspando o titulo e preço de cada livro


# Exemplo do Course

# Define a primeira página como próxima a ter seu conteúdo recuperado
# URL_BASE = "http://books.toscrape.com/catalogue/"
# next_page_url = 'page-1.html'
# while next_page_url:
#     # Busca o conteúdo da próxima página
#     response = requests.get(URL_BASE + next_page_url)
#     selector = Selector(text=response.text)
#     # Imprime os produtos de uma determinada página
#     for product in selector.css(".product_pod"):
#         title = product.css("h3 a::attr(title)").get()
#         price = product.css(".price_color::text").get()
#         print(title, price)
#     # Descobre qual é a próxima página
#     next_page_url = selector.css(".next a::attr(href)").get()