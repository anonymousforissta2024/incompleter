import pandas as pd
import numpy as np
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
sales_tuples = list(zip(*sales_arrays))
print('Create a MultiIndex:')
print(sales_tuples)
print('\nConstruct a series using the said MultiIndex levels: ')
s = pd.Series(np.random.randn(8), index=sales_index)
print(s)