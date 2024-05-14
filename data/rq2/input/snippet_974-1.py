from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Python')
for link in bsObj.findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])