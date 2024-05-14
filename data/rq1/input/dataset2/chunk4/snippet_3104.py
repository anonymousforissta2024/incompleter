#Source: https://stackoverflow.com/questions/23570549/beautiful-soup-error-nameerror-name-htmltext-is-not-defined
from bs4 import BeautifulSoup
import urllib
import urllib.parse

url = "http://nytimes.com"

urls = [url]
visited = [url]

while len(urls) > 0:
        try:
           htmltext = urllib.urlopen(urls[0]).read()
        except:
           print(urls[0])      

        soup = BeautifulSoup(htmltext)    
        urls.pop(0)

        print(soup.findAll('a',href = true))