import pandas as pd
s_dates = pd.Series([0, 1, 2, 3, 4, 5, 6, 7], index=index)
print('Time series object with indexed data:')
print(s_dates)
print('\nDates of same year:')
print(s_dates['2015'])
print('\nDates between 2012-01-01 and 2012-12-31')
print(s_dates['2012-01-01':'2012-12-31'])