import pandas as pd
data1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']}, index=['K0', 'K1', 'K2'])
data2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'], 'D': ['D0', 'D2', 'D3']}, index=['K0', 'K2', 'K3'])
print('Original DataFrames:')
print(data1)
print('--------------------')
print(data2)
print('\nMerged Data (Joining on index):')
print(result)