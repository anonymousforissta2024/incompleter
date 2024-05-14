#Source: https://stackoverflow.com/questions/75155197/typeerror-string-indices-must-be-integers-in-the-time-of-downloading-stock-data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader.data as web
import datetime

start=datetime.datetime(2015,6,1)
end=datetime.datetime(2022,6,30)

sbin=web.DataReader('SBIN.BO','yahoo',start,end)
tatamotors=web.DataReader('TATAMOTORS.BO','yahoo',start,end)
reliance=web.DataReader('RELIANCE.BO','yahoo',start,end)