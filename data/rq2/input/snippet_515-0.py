import pandas as pd
index = pd.DatetimeIndex(['2011-09-02', '2012-08-04', '2015-09-03', '2010-08-04', '2015-03-03', '2011-08-04', '2015-04-03', '2012-08-04'])
print('Time series object with indexed data:')
print(s_dates)
print('\nDates of same year:')
print(s_dates['2015'])
print('\nDates between 2012-01-01 and 2012-12-31')
print(s_dates['2012-01-01':'2012-12-31'])