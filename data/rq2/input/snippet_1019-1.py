import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print('\nTotal missing values in a dataframe:')
tot_missing_vals = df.isnull().sum().sum()
print(tot_missing_vals)