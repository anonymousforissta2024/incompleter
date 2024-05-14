#Source: https://stackoverflow.com/questions/41803669/typeerror-bad-operant-type-for-unary-type-while-extracting-keywords-form
#Loading Libraries
import urllib
import os
from urllib.parse import urlparse
from urllib.parse import urljoin
import urllib.request
from bs4 import BeautifulSoup
id= 1
url='http://scitechdaily.com/new-technique-reveals-internal-characteristics-of-photonic-crystals/'
def getKeywords(articletext):
    common = open('C:\\Users\\Hassan Raza\\Desktop\\Mozilla tech article\\common.txt').read().split('\n')
    word_dict = {articletext:float}
    word_list = articletext.lower().split()
    for word in word_list:
        if word not in common:
            if word not in word_dict:
                word_dict[word] = 1
            if word in word_dict:
                word_dict[word] +=1

    sorteddata = Counter(word_dict).most_common()
    #print(sorted(word_dict.items(),key=lambda kv: (-kv[1], kv[0]),reverse=True))


def GetArticles(url,id):
    file = open('C:\\Users\\Hassan Raza\\Desktop\\Mozilla tech article\\Article'+'.txt', 'w')
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()

    soup = BeautifulSoup(html,"html.parser")

    title= soup.find_all('h1', {'class','title'})
    for titles in title:
        print(titles.text)
    text = soup.find_all('div' , {'class', 'entry'})
    for pg in text:
        articletext=(pg.text.encode('utf8'))
        getKeywords(articletext)

    file.close()

GetArticles(url,id)