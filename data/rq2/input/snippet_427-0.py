import pandas as pd
print('Original Data Series:')
print(s)
s = s.reindex(index=['B', 'A', 'C', 'D', 'E'])
print('Data Series after changing the order of index:')
print(s)