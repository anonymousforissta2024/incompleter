import pandas as pd
print('Original Series of list')
print(s)
s = s.apply(pd.Series).stack().reset_index(drop=True)
print('One Series')
print(s)