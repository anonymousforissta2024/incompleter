#Source: https://stackoverflow.com/questions/59589155/typeerror-unhashable-type-list-when-plotting-multiple-charts
import fxcmpy
import pandas as pd
from pandas import datetime
from pandas import DataFrame as df
import matplotlib
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import datetime
from datetime import date
import numpy as np
TOKEN = "hidden "
con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='error')
print(con.get_instruments())
ticker= con.get_instruments()
def convert(ticker):
    return tuple(ticker)
ticker = convert(ticker)
start = datetime.datetime(2008,1,1)
end = datetime.datetime.today()
today = date.today()
data = con.get_candles(ticker, period='D1', start = start, end = end)
data.index = pd.to_datetime(data.index, format ='%Y-%m-%d')