#Source: https://stackoverflow.com/questions/60261686/attributeerror-list-object-has-no-attribute-timeout
import bs4 as bs
import urllib.request
import urllib.parse 
import re
import nltk
import pandas as pd 
from pandas import DataFrame


nltk.download('stopwords')
import heapq

listofurls = pd.read_csv("C:/Users/Sajid Hasan Sifat/Desktop/global one/GO-url.csv") 
urls = DataFrame(listofurls, columns = ['urls'])
url_list = urls.values.tolist()
print(url_list[0])

req = urllib.request.Request(url_list[0])    
print(req) 
sourceData = urllib.request.urlopen(url_list[0]) 

source = sourceData.read()
soup = bs.BeautifulSoup(source)