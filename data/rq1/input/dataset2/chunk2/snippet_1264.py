#Source: https://stackoverflow.com/questions/62365323/williams-r-ta-lib-getting-typeerror-with-look-back-period
import pandas as pd
# import matplotlib
from pandas_datareader import data as web
import ta


df = web.DataReader('F', 'yahoo')

williams1 = ta.momentum.WilliamsRIndicator(
        high = df['High'], 
        low = df['Low'], 
        close = df['Close'], 
        fillna = False
        )

williams1.wr()