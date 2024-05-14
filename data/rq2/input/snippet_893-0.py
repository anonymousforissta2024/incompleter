import pandas as pd
print('Original Series:')
print(date_series)
print('\nSeries of date strings to a timeseries:')
print(pd.to_datetime(date_series))