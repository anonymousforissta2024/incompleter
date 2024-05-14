#Source: https://stackoverflow.com/questions/67106239/attributeerror-nonetype-object-has-no-attribute-encode-binance
import os

from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor

# Get keys
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

# Connect to Binance
client = Client(api_key, api_secret)
print(client.get_account())