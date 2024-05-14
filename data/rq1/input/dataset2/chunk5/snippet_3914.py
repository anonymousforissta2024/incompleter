#Source: https://stackoverflow.com/questions/59065312/i-am-getting-attributeerror-nonetype-object-has-no-attribute-find-all
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import mysql.connector

page = requests.get("https://www.adelaideairport.com.au/flight-information/flight-search/")
soup = BeautifulSoup(page.content, 'html.parser')
flights = soup.find(id="SearchResultFlightListTable")
flight_items = flights.find_all(class_="row")
flight = flight_items[0]
print(flight.prettify())