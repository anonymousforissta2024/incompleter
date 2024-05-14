#Source: https://stackoverflow.com/questions/71321015/attributeerror-dataframe-object-has-no-attribute-get-data-yahoo-i-am-gett
import copy

import pandas as pd
import talib
import yfinance as yf

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
from pandas_datareader import data as pdr

yf.pdr_override()


def symbol_back_test(symbol):
    global pdr
    pdr = pdr.get_data_yahoo(symbol, period="2y", interval="1d")

    pdr["MA_10"] = talib.MA(pdr["Close"], timeperiod=10)
    pdr["MA_50"] = talib.MA(pdr["Close"], timeperiod=50)
    pdr["RSI_14"] = talib.RSI(pdr["Close"], timeperiod=14)

    position = None
    symbol_trades = []
    trade = {"Symbol": None, "Buy/Sell": None, "Entry": None, "Entry Date": None, "Exit": None, "Exit Date": None}

    for i in pdr.index[49:]:

        if pdr["MA_10"][i] > pdr["MA_50"][i] and pdr["RSI_14"][i] > 50 and position != "Buy":
            if trade["Symbol"] is not None:
                trade["Exit"] = pdr["Close"][i]
                trade["Exit Date"] = i
                symbol_trades.append(copy.deepcopy(trade))
            if position is not None:
                trade["Symbol"] = symbol
                trade["Buy/Sell"] = "Buy"
                trade["Entry"] = pdr["Close"][i]
                trade["Entry Date"] = i

            position = "Buy"
        if pdr["MA_10"][i] < pdr["MA_50"][i] and pdr["RSI_14"][i] < 50 and position != "Sell":
            if trade["Symbol"] is not None:
                trade["Exit"] = pdr["Close"][i]
                trade["Exit Date"] = i
                symbol_trades.append(copy.deepcopy(trade))
            if position is not None:
                trade["Symbol"] = symbol
                trade["Buy/Sell"] = "Sell"
                trade["Entry"] = pdr["Close"][i]
                trade["Entry Date"] = i

            print("Sell")
            position = "Sell"
    return symbol_trades


symbol_list = ["INFY.NS"]
for symbol in symbol_list:
    print(symbol_back_test(symbol))