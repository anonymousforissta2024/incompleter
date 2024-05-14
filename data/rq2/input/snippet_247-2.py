from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, 'html.parser')
print('List all the header tags :', *titles, sep='\n\n')