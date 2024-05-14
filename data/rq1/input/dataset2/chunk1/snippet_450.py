#Source: https://stackoverflow.com/questions/47999393/typeerror-init-got-an-unexpected-keyword-argument-encoding
import pandas as pd
...

url = "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end="+time.strftime("%Y%m%d")

# CODE FAILS HERE
bitcoin_market_info = pd.read_html(url)[0]