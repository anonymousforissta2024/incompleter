import pandas as pd
data2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'], 'D': ['D0', 'D2', 'D3']}, index=['K0', 'K2', 'K3'])
print('Original DataFrames:')
print(data1)
print('--------------------')
print(data2)
print('\nMerged Data (Joining on index):')
result = data1.join(data2)
print(result)