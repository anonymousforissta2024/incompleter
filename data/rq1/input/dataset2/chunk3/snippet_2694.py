#Source: https://stackoverflow.com/questions/54915685/attributeerror-nonetype-object-has-no-attribute-lower-while-trying-to-con
import requests
from bs4 import BeautifulSoup as bs
import operator

def webpage(url):
    word_list = []
    soup = bs(requests.get(url).text, 'html.parser')
    for text in soup('p', {'class': 'PE7lZb'}):
        content = text.string
        words = content.lower().split()

webpage("https://godan.business.site/")