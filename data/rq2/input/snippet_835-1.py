import pandas as pd
import numpy as np
sales_tuples = list(zip(*sales_arrays))
print('Create a MultiIndex:')
sales_index = pd.MultiIndex.from_tuples(sales_tuples, names=['sale', 'city'])
print(sales_tuples)
print('\nConstruct a series using the said MultiIndex levels: ')
s = pd.Series(np.random.randn(8), index=sales_index)
print(s)