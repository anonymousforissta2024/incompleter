import pandas as pd
data1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'], 'key2': ['K0', 'K1', 'K0', 'K1'], 'P': ['P0', 'P1', 'P2', 'P3'], 'Q': ['Q0', 'Q1', 'Q2', 'Q3']})
print('Original DataFrames:')
print(data1)
print('--------------------')
print(data2)
print('\nMerge two dataframes with different columns:')
result = pd.concat([data1, data2], axis=0, ignore_index=True)
print(result)