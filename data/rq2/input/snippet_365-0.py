import pandas as pd
import numpy as np
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
print('Create a MultiIndex:')
sales_index = pd.MultiIndex.from_tuples(sales_tuples, names=['sale', 'city'])
print(sales_tuples)
print('\nConstruct a Dataframe using the said MultiIndex levels: ')
df = pd.DataFrame(np.random.randn(8, 5), index=sales_index)
print(df)