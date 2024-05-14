#Source: https://stackoverflow.com/questions/54922007/trying-to-extract-links-from-fetching-link-from-csv-file-into-request-get-but-ge
from bs4 import BeautifulSoup

import requests

import csv

import pandas as pd

links = pd.read_csv('C:\\Users\\acer\\Desktop\\hindustan_pages.csv',encoding = 'latin',dtype=str)

for i in range(1,3):

      link = links.iloc[i,0]

      r = requests.get(link)

      soup = BeautifulSoup(r.text,'lxml')

      div = soup.find('div',{"id":"company_list_grid"})
      for links in div.find_all('th',{"id":"c_name"}):
          link = links.find('a')
          print("https://www.hindustanyellowpages.in/Ahmedabad" + link['href'][2:])