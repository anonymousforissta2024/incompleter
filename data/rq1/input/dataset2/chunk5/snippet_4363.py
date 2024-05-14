#Source: https://stackoverflow.com/questions/70636568/when-executing-the-program-it-gives-an-error-typeerror-list-indices-must-be-i
import requests

from datetime import datetime

def get_from_binance():

    req = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    response = req.json()
    sell_price = response["price"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\nBTC Binance: {sell_price}")


def get_from_bittrex():

    req2 = requests.get("https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC")
    response2 = req2.json()
    sell_price2 = response2["result"]['Last']
    print(f"BTC Bittrex: {sell_price2}")


def get_from_bitfinex():

    req3 = requests.get("https://api-pub.bitfinex.com/v2/tickers?symbols=tBTCUSD")
    response3 = req3.json()
    sell_price3 = response3["0"]["1"]
    print(f"BTC bitfinex: {sell_price3}")


if __name__ == '__main__':

    get_from_binance()
    get_from_bittrex()
    get_from_bitfinex()