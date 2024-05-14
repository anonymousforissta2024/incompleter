#Source: https://stackoverflow.com/questions/65459802/typeerror-on-pandas-dataframe
import pandas as pd
from datetime import datetime,timedelta

data=pd.read_csv("Dataset.csv",low_memory=False)
data.Date = data.Date.apply(lambda x:datetime.strptime(x, '%Y-%m-%d'))