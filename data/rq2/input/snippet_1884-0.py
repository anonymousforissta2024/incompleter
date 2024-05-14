import pandas as pd
print('Given Dataframe is :\n', df)
print("\nSplitting 'Name' column into two different columns :\n", df.Name.str.split(expand=True))