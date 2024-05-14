import pandas as pd
dataframe = pd.DataFrame(record, columns=['Name', 'Age', 'Stream', 'Percentage'])
print('Given Dataframe :\n', dataframe)
rslt_df = dataframe[dataframe['Percentage'] > 80]
print('\nResult dataframe :\n', rslt_df)