#Source: https://stackoverflow.com/questions/47380110/python-attribute-error-nonetype-object-has-no-attribute-find-all
from bs4 import BeautifulSoup
from urllib.request import urlopen
url='https://simple.wikipedia.org/wiki/List_of_U.S._states'
web=urlopen(url)
source=BeautifulSoup(web, 'html.parser')
table=source.find('table', {'class': 'wikitable sortable jquery-tablesorter'})
abbs=table.find_all('b')
print(abbs.get_text())