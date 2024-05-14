#Source: https://stackoverflow.com/questions/55668134/how-do-i-fix-the-attributeerror-nonetype-object-has-no-attribute-text-whe
import requests

from bs4 import BeautifulSoup

import csv

import lxml


# Lists to store the scraped data in

addresses = []
geographies = []
rents = []
units = []
availabilities = []

# Scraping all pages

pages_url = requests.get('https://www.rent.com/new-york/tuckahoe-apartments')

pages_soup = BeautifulSoup(pages_url.text, 'html.parser')

list_nums = pages_soup.find('div', class_='_1y05u').text

print(list_nums)

pages = [str(i) for i in range(1,8)]

for page in pages:

    response = requests.get('https://www.rent.com/new-york/tuckahoe-apartments?page=' + page).text

    html_soup = BeautifulSoup(response, 'lxml')


    # Extract data from individual listing containers

    listing_containers = html_soup.find_all('div', class_='_3PdAH')
    print(type(listing_containers))
    print(len(listing_containers))



    for container in listing_containers:
        address = container.a.text
        addresses.append(address)

        geography = container.find('div', class_='_1dhrl').text
        geographies.append(geography)

        rent = container.find('div', class_='_3e12V').text
        rents.append(rent)

        unit = container.find('div', class_='_2tApa').text
        units.append(unit)

        availability = container.find('div', class_='_2P6xE').text
        availabilities.append(availability)

        import pandas as pd
        test_df = pd.DataFrame({'Street' : addresses,
                                'City-State-Zip' : geographies,
                                'Rent' : rents,
                                'BR/BA' : units,
                                'Units Available' : availabilities

        })
        print(test_df)