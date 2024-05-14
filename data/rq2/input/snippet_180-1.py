import pandas as pd
df = pd.DataFrame({'year': [2018, 2019, 2020], 'month': [2, 3, 4], 'day': [4, 5, 6], 'hour': [2, 3, 4]})
print('Original dataframe:')
print(df)
print('\nSeries of Timestamps from the said dataframe:')
print(result)
print('\nSeries of Timestamps using specified columns:')
print(pd.to_datetime(df[['year', 'month', 'day']]))