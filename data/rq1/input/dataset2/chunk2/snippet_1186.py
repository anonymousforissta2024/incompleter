#Source: https://stackoverflow.com/questions/76077843/why-is-my-code-giving-me-an-attributeerror
import requests
from bs4 import BeautifulSoup

url = 'https://www.ilga.gov/legislation/default.asp'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the House Bills section
house_bills = soup.find('a', {"name": "h_bills"}).parent

# Iterate through all links in the House Bills section
for link in house_bills.find_all('a'):
    href = link.get('href')
    if href.startswith('/legislation/BillStatus.asp?'):
        bill_url = url + href
        bill_response = requests.get(bill_url)
        bill_soup = BeautifulSoup(bill_response.content, 'html.parser')

        # Find the table cell with width
        td = bill_soup.find('td', {'width': '100%'})
        
        # Iterate through all the <li> elements in table
        for li in td.find_all('li'):
            print(li.text)   