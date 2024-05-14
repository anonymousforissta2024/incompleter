import pandas as pd
import numpy as np
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
sales_tuples = list(zip(*sales_arrays))
print(sales_tuples)
print('\nConstruct a Dataframe using the said MultiIndex levels: ')
df = pd.DataFrame(np.random.randn(8, 5), index=sales_index)
print(df)
print('\nSort on MultiIndex DataFrame:')
df1 = df.sort_index()
print('\nSort on Index level=0 of the DataFrame:')
df2 = df.sort_index(level=0)
print(df2)
print('\nSort on Index level=1 of the DataFrame:')
df2 = df.sort_index(level=1)
print(df2)
print('\nPass a level name to sort the DataFrame:')
df3 = df.sort_index(level='city')
print(df3)