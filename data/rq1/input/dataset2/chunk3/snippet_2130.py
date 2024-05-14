#Source: https://stackoverflow.com/questions/71508606/attributeerror-navigablestring-object-has-no-attribute-keys-in-python
import requests
import csv
from bs4 import BeautifulSoup as bs

global newsitems
def loadRSS():
    url="https://rss.nytimes.com/services/xml/rss/nyt/Africa.xml"
    resp=requests.get(url)
    with open('topnewsfeed.xml','wb') as f:
        f.write(resp.content)

def extractData():
    infile = open("topnewsfeed.xml","r",encoding='utf-8')
    contents = infile.read()
    soup = bs(contents,'xml')
    guids= soup.find_all('guid')
    titles = soup.find_all('title')
    pubDates= soup.find_all('pubDate')
    descs= soup.find_all('description')
    links= soup.find_all('link')
    newsitems=[]
    for (guid,title,pubDate,desc,link) in zip(guids,titles,pubDates,descs,links):
        newsitems.append(guid.string)
        newsitems.append(title.string)
        newsitems.append(pubDate.string)
        newsitems.append(desc.string)
        newsitems.append(link.string)
    return newsitems

def savetoCSV(array,filename):
    fields=['Guid','Title','PubDate','Description','Link']
    with open(filename,'w') as csvfile:
        writer=csv.DictWriter(csvfile,fieldnames=fields)
        writer.writeheader()
        writer.writerows(array)
             
def run():
    loadRSS()
    newsitems=extractData()
    savetoCSV(newsitems,'topnews.csv')
run()