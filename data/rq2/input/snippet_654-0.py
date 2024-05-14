import pandas as pd
sr1 = pd.Series([1, 2, 3, 4, 5])
print('Original Series:')
print('sr1:')
print(sr1)
print('sr2:')
print(sr2)
print('\nItems of sr1 not present in sr2:')
result = sr1[~sr1.isin(sr2)]
print(result)