#Source: https://stackoverflow.com/questions/64014172/beautifulsoup-attributeerror-when-using-find-all-on-multiple-tables
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/2020%E2%80%9321_Top_14_season'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')
match = soup.find_all('.vevent summary')

#for table in match.find_all('table'):
for data in match.find_all('tbody'):
    for row in data.find('tr'):
        for cell in row.find('td'):
            print (cell.text.replace('&nbsp;', ''))