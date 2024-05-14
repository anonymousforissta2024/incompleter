import pandas as pd
import numpy as np
sales_tuples = list(zip(*sales_arrays))
sales_index = pd.MultiIndex.from_tuples(sales_tuples, names=['sale', 'city'])
print(sales_tuples)
print('\nConstruct a Dataframe using the said MultiIndex levels: ')
df = pd.DataFrame(np.random.randn(8, 5), index=sales_index)
print(df)
print('\nRename the columns name of the said dataframe')
df1 = df.rename(columns={0: 'col1', 1: 'col2', 2: 'col3', 3: 'col4', 4: 'col5'})
print(df1)
print('\nRename specific labels of the main index of the DataFrame')
df2 = df1.rename(index={'sale2': 'S2', 'city2': 'C2'})
print(df2)