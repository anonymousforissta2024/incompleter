#Source: https://stackoverflow.com/questions/52020762/beautifulsoup-attributeerror-navigablestring-object-has-no-attribute-find
import pandas as pd
from bs4 import BeautifulSoup
import requests
import lxml.html as lh


with open("htmltabletest.html", encoding="utf-8") as f:
    data = f.read()
    soup = BeautifulSoup(data, 'lxml')
    for table in soup.find('table', attrs={'id': 'eventSearchTable'}):
        for rows in table.find_all('tr'):
            cols = table.find_all('td')

            empty = cols[0].get_text()
            eventdate = cols[1].get_text()
            eventname = cols[2].get_text()
            tickslisted = cols[3].get_text()
            pricerange = cols[4].get_text()

            entry = (empty, eventdate, eventname, tickslisted, pricerange)

            print(entry)