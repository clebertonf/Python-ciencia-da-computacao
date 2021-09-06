# python3 -m pip install parsel

from parsel import Selector
import requests

# Fazendo um requisição
response = requests.get('http://books.toscrape.com/')
# Extraindo dados
selector = Selector(text=response.text)
# print(selector)

titles = selector.css(".product_pod h3 a::attr(title)").getall()

prices = selector.css(".product_price .price_color::text").getall()

for indice in range(len(titles)):
    print(f'Nome: {titles[indice]} Preco: {prices[indice]}')

