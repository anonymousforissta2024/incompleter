import pandas as pd
newday = pd.Timestamp('2020-02-07')
print('First date:')
print(newday)
print('\nThe day name of the said date:')
print(newday.day_name())
print('\nAdd 2 days with the said date:')
print(newday1.day_name())
print('\nNext business day:')
nbday = newday + pd.offsets.BDay()
print(nbday.day_name())