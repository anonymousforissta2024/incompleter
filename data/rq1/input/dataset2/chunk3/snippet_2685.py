#Source: https://stackoverflow.com/questions/68656775/attributeerror-set-object-has-no-attribute-items-python-product-in-stock-ch
from bs4 import BeautifulSoup
import requests
import time

def get_page_html(URL):
    headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    page = requests.get(url, headers=headers)
    print(page.status_code)
    return page.content


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_div = soup.find("div", {"id": "sold_out_text"})
    return out_of_stock_div.text == "In stock."

def check_inventory():
    url = "https://www.boots.com/dyson-v10-cyclone-animal-10267801" 
    page_html = get_page_html(URL)
    if check_item_in_stock(page_html):
        print("In stock")
    else:
        print("Out of stock")

while True:
    check_inventory()
    time.sleep(60)