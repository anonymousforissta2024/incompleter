#Source: https://stackoverflow.com/questions/75953316/python3-attributeerror-nonetype-object-has-no-attribute-find-all
import requests
from bs4 import BeautifulSoup

url = 'https://otakudesu.lol/genre-list/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

genres_div = soup.find('div', class_='genres')
genre_links = genres_div.find_all('a')

path = []
text = []

for link in genre_links:
    path.append(link['href'])
    text.append(link.text)

print(path)
print(text)