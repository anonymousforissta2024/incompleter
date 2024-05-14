#Source: https://stackoverflow.com/questions/59132467/concat-2-columns-in-pandas-attributeerror-dataframe-object-has-no-attribute
import pandas as pd
import numpy as np
from statsmodels import api as sm
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2015,2,12)
end = datetime.datetime.today()
df = web.get_data_yahoo(['F', '^GSPC'], start, end)

df1 = df.concat(columns=[F['Close'], gspc['Close']], axis=1)