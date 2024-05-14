import pandas as pd
from pandas.tseries.offsets import *
import datetime
from datetime import datetime, date
dt = datetime(2020, 1, 4)
print('Specified date:')
print(dt)
print('\nOne business day from the said date:')
obday = dt + BusinessDay()
print(obday)
print('\nTwo business days from the said date:')
tbday = dt + 2 * BusinessDay()
print(tbday)
print('\nThree business days from the said date:')
thbday = dt + 3 * BusinessDay()
print(thbday)
print('\nNext business month end from the said date:')
print(nbday)