#Source: https://stackoverflow.com/questions/73877049/attributeerror-nonetype-object-has-no-attribute-find-beautifulsoup
from bs4 import BeautifulSoup
import requests

def cryptoPrice(crypto):
    url = "https://www.google.com/search?q=" + crypto + "price"

    req = requests.get(url)

    soupObject = BeautifulSoup(req.text, 'html.parser')
    element = soupObject.find("div", {"class": "card-section PZPZlf"}).find("div").find("span", {"class": 'pclqee'}).text

    return element


price = cryptoPrice('bitcoin')
print(price)