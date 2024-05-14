#Source: https://stackoverflow.com/questions/69006489/downloading-image-from-url-filenotfounderror-errno-2-no-such-file-or-direct
import requests
import os
from bs4 import BeautifulSoup

from downloader import download

url = 'https://urltoimage.com/123456/apple-banana-carrot-dog-electric-fish-gorilla-horse-igloo-jackrabbit-kangaroo-long-maze-nickel-octopus-pretty/'
model_name = 'Coolname'

album_name = ' '.join(url.split("/")).split()[-1] #apple-banana-carrot-dog-electric-fish-gorilla-horse-igloo-jackrabbit-kangaroo-long-maze-nickel-octopus-pretty
print("Album name: " + album_name)
location = "C:/Users/Dave/Desktop/" + model_name + "/" + album_name + "/"

print('Location: ' + location) #C:/Users/Dave/Desktop/Coolname/apple-banana-carrot-dog-electric-fish-gorilla-horse-igloo-jackrabbit-kangaroo-long-maze-nickel-octopus-pretty/

reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

for link in soup.find_all('img'):
    if album_name in link.get('src').lower():
        print(link.get('src'))
        download(link.get('src'), location)