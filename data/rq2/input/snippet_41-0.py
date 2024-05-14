import pandas as pd
print('Original Series:')
print(series1)
result = series1.map(lambda x: len(x))
print('\nNumber of characters in each word in the said series:')
print(result)