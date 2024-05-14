#Source: https://stackoverflow.com/questions/46673298/python-attributeerror-stock-analysis-object-has-no-attribute-stock-data
#! /usr/bin/python3
# -*- coding: utf-8 -*-
from pandas_datareader import data as pdr
import quandl

class Stock_Analysis:
    def __init__(self, Stock_Ticker,Start_Date):    
        self.ticker = Stock_Ticker
        self.start_date = Start_Date
        try:
            self.stock_data = pdr.get_data_yahoo(self.ticker,self.start_date)
        except:
            print("Error with Yahoo - please enter Quandl Tickers")
            try:
                self.quandl_ticker = input()
                self.stock_data = quandl.get(self.quandl_ticker)
            except:
                "Failled"
    def Print_Data(self):
        print(self.stock_data)

apple = Stock_Analysis("AAPL","2015-01-01")
apple.Print_Data()