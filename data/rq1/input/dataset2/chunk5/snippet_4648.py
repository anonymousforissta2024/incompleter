#Source: https://stackoverflow.com/questions/61487693/nameerror-name-soup-is-not-defined
import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.ca/QuietComfort-Wireless-Headphones-Cancelling-Control/dp/B0756CYWWD/ref=sr_1_3?crid=11Q0SFC2UP92R&keywords=bose+quietcomfort+35&qid=1588098577&s=electronics&sprefix=bose+q%2Celectronics%2C160&sr=1-3'
r = requests.get(url)
data = BeautifulSoup(r.text, 'html.parser')
original_price = soup.find(id = "priceblock_ourprice")
print(original_price)