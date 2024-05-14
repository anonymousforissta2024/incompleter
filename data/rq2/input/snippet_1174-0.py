import pandas as pd
print('Original Data Series:')
print(s)
print('\nData Series after adding some data:')
new_s = s.append(pd.Series(['500', 'php']))
print(new_s)