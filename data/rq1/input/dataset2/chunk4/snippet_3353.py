#Source: https://stackoverflow.com/questions/75637456/typeerror-a-bytes-like-object-is-required-not-str-python-3-bs4
# LIBRAIRIES

import requests
from bs4 import BeautifulSoup
import csv


# SEARCH URL

url = 'https://www.atlas-monde.net/tous-les-pays/'
response = requests.get(url)

# EXTRACT DATAS

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    # items = soup.find_all(class_="sidebar")
    items = soup.find_all("td")
    for i in items:
        print(i.string + '\n')


# CREATE DATAS FIELD

with open('persons.csv', 'wb') as csvfile:
    for item in items:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(item)