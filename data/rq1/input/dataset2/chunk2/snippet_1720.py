#Source: https://stackoverflow.com/questions/50798940/beautifulsoup-and-regexp-attribute-error
import requests
from bs4 import BeautifulSoup
import re

url = 'https://inventaris.onroerenderfgoed.be/erfgoedobjecten/4778'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
text = soup.prettify()

##block
p = re.compile('(?s)(?<=(Typologie))(.*?)(?=(</a>))', re.VERBOSE)
block = p.search(text).group(2)


##typo_url
p = re.compile('(?s)(?<=(href=\"))(.*?)(?=(\">))', re.VERBOSE)
typo_url = p.search(block).group(2)


## typo_name
p = re.compile('\b(\w+)(\W*?)$', re.VERBOSE)
typo_name = p.search(block).group(1)