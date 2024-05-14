#Source: https://stackoverflow.com/questions/67284107/python-attributeerror-super-object-has-no-attribute-testnet-however-the-at
from binance.client import Client
from binance.websockets import BinanceSocketManager

class Binance_Data(Client):
    def __init__(self, api_key, api_secret, requests_params=None, tld='us'):
        super().__init__(api_key, api_secret, requests_params=None, tld='us')

    def data_stream_test(self, data):
        print('------------------')
        print(f"Event Title: {data['e']}")
        print(f"Closing Price: {data['c']}")
        print(convert_unix_to_utc(data['E']))
        print('------------------')

    def data_stream(self):
        ds = BinanceSocketManager(super())
        conn_key = ds.start_symbol_ticker_socket('XLMUSDT', data_stream_test)
        ds.start()