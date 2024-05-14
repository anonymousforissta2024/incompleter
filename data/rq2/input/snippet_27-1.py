import pandas as pd
print('Original Data Series:')
print(s)
print('\nSubset of the above Data Series:')
n = 6
new_s = s[s < n]
print(new_s)