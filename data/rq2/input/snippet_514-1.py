import pandas as pd
print('Create a dataframe, indexing by date and time:')
dt_range = pd.date_range(start='2020-05-12 07:10:10', freq='S', periods=10)
print(df_dt)