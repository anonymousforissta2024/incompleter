import pandas as pd
print('Convert integer or float epoch times to Timestamp and DatetimeIndex upto second:')
print(dates1)
print('\nConvert integer or float epoch times to Timestamp and DatetimeIndex upto milisecond:')
dates2 = pd.to_datetime([1249720105100, 1249720105200, 1249720105300, 1249720105400, 1249720105500], unit='ms')
print(dates2)