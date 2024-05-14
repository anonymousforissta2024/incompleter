#Source: https://stackoverflow.com/questions/62947923/attributeerror-nonetype-object-has-no-attribute-contains
import requests    
from bs4 import BeautifulSoup    
import pandas as pd    
import pdfkit    
import re        

URL = 'https://timesofindia.indiatimes.com/'    

page = requests.get(URL)    
soup = BeautifulSoup(page.content, 'lxml')    
page = requests.get(URL)    
soup = BeautifulSoup(page.content, 'lxml')    
all_links=set()    

for link in soup.find_all('a'):    
    all_links.add(link.get('href'))    

s = list(all_links)     
print(s)    
x=[i for i in s if i._contains_(URL)]    
m=[]    
find_words= ['cbse', 'first-day']    
for s in x:    
    if any(f in s for f in find_words):    
        m.append(s)    
print(m)