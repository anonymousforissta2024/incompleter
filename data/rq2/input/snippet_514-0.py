import pandas as pd
print('Create a dataframe, indexing by date and time:')
df_dt = pd.DataFrame({'Sale_amt': [100, 110, 117, 150, 112, 99, 129, 135, 140, 150]}, index=dt_range)
print(df_dt)