import pandas as pd
print('Original dataframe:')
print(df)
result = pd.to_datetime(df)
print('\nSeries of Timestamps from the said dataframe:')
print(result)
print('\nSeries of Timestamps using specified columns:')
print(pd.to_datetime(df[['year', 'month', 'day']]))