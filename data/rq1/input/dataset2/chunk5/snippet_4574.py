#Source: https://stackoverflow.com/questions/69457805/i-am-taking-data-from-an-api-but-i-get-the-error-message-typeerror-list-indic
import requests
import json
from bs4 import BeautifulSoup
link = requests.get('https://api.hypixel.net/skyblock/bazaar')
data = link.text
dictionary = json.loads(data)
print(str(dictionary['products']['BROWN_MUSHROOM']['sell_summary']['sellPrice']))