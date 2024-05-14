import pandas as pd
dates1 = pd.to_datetime([1329806505, 129806505, 1249892905, 1249979305, 1250065705], unit='s')
print('Convert integer or float epoch times to Timestamp and DatetimeIndex upto second:')
print(dates1)
print('\nConvert integer or float epoch times to Timestamp and DatetimeIndex upto milisecond:')
print(dates2)