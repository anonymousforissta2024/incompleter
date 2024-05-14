#Source: https://stackoverflow.com/questions/56744083/attributeerror-str-object-has-no-attribute-descendants-error-when-using-bea
from bs4 import BeautifulSoup, SoupStrainer
import requests

url = "https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3210001601"
page = requests.get(url)
data = page.text
soup = BeautifulSoup
soup.find_all('h1')

print(text)