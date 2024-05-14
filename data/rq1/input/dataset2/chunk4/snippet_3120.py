#Source: https://stackoverflow.com/questions/63840124/error-while-using-beautifulsoup-in-python-attribute-error
from bs4 import BeautifulSoup
import urllib.request

with open('websites_mn.txt') as f:
    txtdata = f.readlines()

for raw_url in txtdata:
    raw_url = raw_url.strip('\n')
    url = urllib.request.urlopen(raw_url)
    content = url.read()
    soup = BeautifulSoup(content, 'lxml')
    table = soup.findAll('div',attrs={"class":"journal-content-article"})
    for x in table:
        print(x.find('p').text)