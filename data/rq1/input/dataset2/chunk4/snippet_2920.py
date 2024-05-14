#Source: https://stackoverflow.com/questions/76716939/request-getpage-typeerror-cannot
# -*- coding: utf-8 -*-

from twisted.web.client import ProxyAgent
from twisted.web import client

url="http://www.opensubtitles.org/libs/suggest.php?format=json2&SubLanguageID=null&MovieName=red"

headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
          'Upgrade-Insecure-Requests': '1',
          'Content-Type': 'application/x-www-form-urlencoded',
          'Referer': url,
          'Connection': 'keep-alive',
          'Accept-Encoding':'gzip, deflate'}

def downloadChunks():

    d = client.getPage(url, contextFactory=None, method="GET", headers=headers)
    print(d)
 
downloadChunks()