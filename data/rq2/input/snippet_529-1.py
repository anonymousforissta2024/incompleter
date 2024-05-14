import pandas as pd
print('Original Data Series:')
print(s)
new_s = pd.Series(s).sort_values()
print(new_s)