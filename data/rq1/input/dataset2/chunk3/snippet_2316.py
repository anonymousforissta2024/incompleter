#Source: https://stackoverflow.com/questions/67344205/pybacktest-library-hello-world-error-builtins-attributeerror-series-object-h
import matplotlib
import matplotlib.pyplot as plt
import pybacktest
import pandas as pd

short_ma = 50
long_ma = 200

ohlc = pybacktest.load_from_yahoo('AAPL', start=2000)
ohlc.tail()

ms = ohlc.C.rolling(short_ma).mean()
ml = ohlc.C.rolling(long_ma).mean()

buy = cover = (ms > ml) & (ms.shift() < ml.shift())  # ma cross up
sell = short = (ms < ml) & (ms.shift() > ml.shift())  # ma cross down

bt = pybacktest.Backtest(locals(), 'ma_cross')

print(bt.summary())

bt.plot_equity()