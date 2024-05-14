import pandas as pd
dataframe = pd.DataFrame(data, columns=['Month', 'Expense'])
print('Given Dataframe :\n', dataframe)
pd.options.display.float_format = '{:.2f}'.format
print('\nResult :\n', dataframe)