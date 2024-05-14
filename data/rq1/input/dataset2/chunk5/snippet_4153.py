#Source: https://stackoverflow.com/questions/59652669/attributeerror-module-pandas-compat-has-no-attribute-binary-type
import pandas_datareader as web
import pandas as pd

df = web.DataReader('RTSI', 'moex', start='2015-01-01', end='2019-12-30')
df