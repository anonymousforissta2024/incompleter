import pandas as pd
import numpy as np
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
sales_tuples = list(zip(*sales_arrays))
sales_index = pd.MultiIndex.from_tuples(sales_tuples, names=['sale', 'city'])
print('\nConstruct a Dataframe using the said MultiIndex levels:')
print(df)
print('\nSelect 1st, 2nd and 3rd row of the said DataFrame:')
positions = [1, 2, 5]
print(df.take([1, 2, 5]))
print('\nTake elements at indices 1 and 2 along the axis 1 (column selection):')
print(df.take([1, 2], axis=1))
print('\nTake elements at indices 4 and 3 using negative integers along the axis 1 (column selection):')
print(df.take([-1, -2], axis=1))