import pandas as pd
import datetime
from datetime import datetime, date
today = datetime(2012, 10, 30)
print('Current date:', today)
tomorrow = today + pd.Timedelta(days=1)
print('Tomorrow:', tomorrow)
yesterday = today - pd.Timedelta(days=1)
print('Yesterday:', yesterday)
date2 = datetime(2016, 7, 19)
print('\nDifference between two dates: ', date1 - date2)