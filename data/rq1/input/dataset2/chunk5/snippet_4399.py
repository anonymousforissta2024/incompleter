#Source: https://stackoverflow.com/questions/56902630/attributeerror-nonetype-object-has-no-attribute-find-all
import requests
from bs4 import BeautifulSoup


# Collect and parse first page
page = requests.get('https://www.jiosaavn.com/album/vijayashanti-birthday-telugu-hits/A05RmafpUiI_')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
artist_name_list = soup.find(class_='song-wrap')

# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')

for artist_name in artist_name_list_items:
    print(artist_name.prettify())