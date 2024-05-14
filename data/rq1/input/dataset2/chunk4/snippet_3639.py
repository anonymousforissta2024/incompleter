#Source: https://stackoverflow.com/questions/73760092/why-do-i-get-an-empty-list-while-scraping-website-and-end-in-type-error
import requests
from bs4 import  BeautifulSoup
import pandas as pd
from urllib import response


kitapurl = "https://1000kitap.com/alintilar"

response = requests.get(kitapurl)
soup = BeautifulSoup(response.content,"html.parser")
gelen_ana_veri= soup.find_all('meta',attrs={'property':'og:description'})['content']
print(gelen_ana_veri)