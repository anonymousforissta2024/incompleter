#Source: https://stackoverflow.com/questions/64491101/i-can-not-scrape-google-news-with-beautiful-soup-i-am-getting-the-errortypeerr
from bs4 import BeautifulSoup
from urllib.request import urlopen

page_info=urlopen('https://news.google.com')
soup=BeautifulSoup(page_info,'html.parser')
headlines=soup.findall('div',{'jscontroller':'d0DtYd'})
for head in headlines:
    headline=head.find('h3').find('a').get_text()
    print(headline)