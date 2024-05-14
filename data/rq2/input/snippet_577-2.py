import pandas as pd
data1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'], 'key2': ['K0', 'K1', 'K0', 'K1'], 'P': ['P0', 'P1', 'P2', 'P3'], 'Q': ['Q0', 'Q1', 'Q2', 'Q3']})
print('Original DataFrames:')
print(data1)
print('--------------------')
print(data2)
print('\nMerged Data:')
merged_data = pd.merge(data1, data2, on=['key1', 'key2'])
print(merged_data)