#Source: https://stackoverflow.com/questions/57275824/matplotlib-error-attributeerror-int-object-has-no-attribute-toordinal
from pandas_datareader import data
import matplotlib.pyplot as plt
from mpl_finance import candlestick2_ohlc
import matplotlib.dates as mdates
import fix_yahoo_finance as yf
import datetime

start = datetime.date(2018, 1, 1)
end = datetime.date.today()

aapl = yf.download("AAPL",start,end) 
aapl.reset_index(inplace=True)

aapl['Date'] = aapl.index.map(mdates.date2num)

fig, ax = plt.subplots()
plt.xlabel("Date")
plt.ylabel("Price")

candlestick2_ohlc(ax, aapl.Open, aapl.High, aapl.Low, aapl.Close, width=1, colorup='g')
plt.savefig('my_figure.png')
plt.show() 