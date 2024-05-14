import pandas as pd
data = {'Month': ['January', 'February', 'March', 'April'], 'Expense': [21525220.653, 31125840.875, 23135428.768, 56245263.942]}
print('Given Dataframe :\n', dataframe)
pd.options.display.float_format = '{:.2f}'.format
print('\nResult :\n', dataframe)