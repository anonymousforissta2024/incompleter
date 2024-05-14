#Source: https://stackoverflow.com/questions/61983027/typeerror-list-indices-must-be-integers-or-slices-not-str-why-list-indexes-are
import requests
from bs4 import BeautifulSoup
import urllib.request
import re

with open('crawlingweb.csv')as f:
    content=f.readlines()
    content=[x.strip() for x in content]

for i in content:
    content[i].replace('[', '').replace(']', '')
    req = requests.get(content[i])
    html = req.text
    data = re.sub('[^0-9a-zA-Z\\s\\.\\,]', '', string=html).lower()
    data = re.sub('<[^>]*>', '', string=html)
    data = re.sub('[^ ㄱ-ㅣ가-힣]+', '', string=html)
    print(data)