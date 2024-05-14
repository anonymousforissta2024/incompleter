import pandas as pd
sr_data = pd.Series([68, 75, 86, 80, None])
print('Original DataFrame:')
print(df_data)
print('\nOriginal Series:')
print(sr_data)
print('\nCheck for inequality of the said series & dataframe:')
print(df_data.ne(sr_data, axis=0))