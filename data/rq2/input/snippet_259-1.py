import pandas as pd
data1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']}, index=['K0', 'K1', 'K2'])
print('Original DataFrames:')
print(data1)
print('--------------------')
print(data2)
print('\nMerged Data (Joining on index):')
result = data1.join(data2)
print(result)