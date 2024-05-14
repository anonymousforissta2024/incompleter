#Source: https://stackoverflow.com/questions/54435328/numpy-typeerror-could-not-be-cast-from-dtypem8us-to-dtypem8d
import numpy as np
import pandas_market_calendars as mcal
from datetime import datetime
import pandas as pd

nyse = mcal.get_calendar('NYSE')
holidays = nyse.holidays()
holidays = list(holidays.holidays) # NYSE Holidays

today = datetime.now()
expiration = datetime(2019,2,13,0,0)

days_to_expiration = np.busday_count(today,expiration,holidays=holidays)
print(days_to_expiration)