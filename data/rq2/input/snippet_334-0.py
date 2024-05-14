import pandas as pd
print('Original DataFrame with single index:')
print(df)
print('\nDataFrame without index:')
print(df.to_string(index=False))