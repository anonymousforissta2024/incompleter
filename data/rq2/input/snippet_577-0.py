import pandas as pd
data2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'], 'key2': ['K0', 'K0', 'K0', 'K0'], 'R': ['R0', 'R1', 'R2', 'R3'], 'S': ['S0', 'S1', 'S2', 'S3']})
print('Original DataFrames:')
print(data1)
print('--------------------')
print(data2)
print('\nMerged Data:')
merged_data = pd.merge(data1, data2, on=['key1', 'key2'])
print(merged_data)