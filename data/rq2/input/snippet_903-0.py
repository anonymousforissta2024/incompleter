import pandas as pd
print('Subtract two timestamps of same time zone:')
date1 = pd.Timestamp('2019-03-01 12:00', tz='US/Eastern')
print('Difference: ', date2 - date1)
print('\nSubtract two timestamps of different time zone:')
date1 = pd.Timestamp('2019-03-01 12:00', tz='US/Eastern')
date2 = pd.Timestamp('2019-03-01 07:00', tz='US/Pacific')
print('Difference: ', date1.tz_localize(None) - date2.tz_localize(None))