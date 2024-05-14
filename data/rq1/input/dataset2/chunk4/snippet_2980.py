#Source: https://stackoverflow.com/questions/46841991/python-3-6-beautifulsoup4-parse-table-attributeerror-resultset-object-has-no
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import re

## Python 3.6
##BeautifulSoup4
def get_all_cities(html_soup):
    """Scrape WIkipedia page for cities in California (https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_California)
    and returns a structured list of city names, county, population, area, and incorporation date"""
    cities_in_california = []
    table_wiki = html_soup.findAll('table', attrs={"class":"wikitable"})
    table_wiki_rows = table_wiki.findAll('tr')
    for rows in table_wiki:
        table_rows_header = html_soup.findAll('th')
        table_rows = html_soup.findAll('td')
        city_entry = {
                'City_name' : table_rows_header[0].text,
                'City_type' : table_rows[1].text,
                'County' : table_rows[2].text,
                'Population' : table_rows[3].text,
                'Area_sqr_miles' : table_rows[4].text,
                'Area_sqr_km' : table_rows[5].text,
                'Incorporation_Date' : table_rows[6].text                
                }
        cities_in_california.append(city_entry)
    return cities_in_california

html = urlopen('https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_California')
html_soup = BeautifulSoup(html, 'html.parser')
city_list = get_all_cities(html_soup)

df = pd.DataFrame(city_list )
df.head(7)