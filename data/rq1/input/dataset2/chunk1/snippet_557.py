#Source: https://stackoverflow.com/questions/52898498/attributeerror-when-using-beautifulsoup
import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.perfectimprints.com/custom-promos/20492/Beach-Balls.html')
source = BeautifulSoup(url.text, 'html.parser')

product_feed = source.find('div', id_="pageBody")

products = product_feed.find_all('div', class_="product_wrapper")

single_product = products[0]

product_name = single_product.find('div', class_="product_name")
product_name = product_name.a.text

sku = single_product.find('div', class_="product_sku")
sku = sku.text

def get_product_details(product):
  product_name = product.find('div', class_="product_name").a.text
  sku = single_product.find('div', class_="product_sku").text
  return {
    "product_name": product_name,
    "sku": sku
  }

all_products = [get_product_details(product) for product in products]
print(all_products)