import pandas as pd
print('Original Series:')
print(ds)
print('\nIndex of 11 in the said series:')
x = ds[ds == 11].index[0]
print(x)