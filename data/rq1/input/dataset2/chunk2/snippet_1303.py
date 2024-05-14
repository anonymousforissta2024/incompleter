#Source: https://stackoverflow.com/questions/46586419/python-attributeerror-nonetype-object-has-no-attribute-fileno
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
style.use('ggplot')
start=dt.datetime(2000,1,1)
end=dt.datetime(2016,12,31)
df= web.DataReader('ERIE', 'google', start, end)
print(df.head())