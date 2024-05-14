import pandas as pd
data2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'], 'key2': ['K0', 'K0', 'K0', 'K0'], 'R': ['R0', 'R1', 'R2', 'R3'], 'S': ['S0', 'S1', 'S2', 'S3']})
print('Original DataFrames:')
print(data1)
print('--------------------')
print(data2)
print('\nMerge two dataframes with different columns:')
result = pd.concat([data1, data2], axis=0, ignore_index=True)
print(result)