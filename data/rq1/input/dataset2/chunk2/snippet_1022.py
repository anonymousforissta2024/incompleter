#Source: https://stackoverflow.com/questions/74097041/attributeerror-list-object-has-no-attribute-decode-im-getting-this-error-w
import csv
import requests
from bs4 import BeautifulSoup 
import wget  
with open('__memes_magic_thumbnails.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
print(data)
k=0
for link in data:
     print(k)
     
     wget.download(link , "vid/logo.jpg")
     k+=1

print("succes")