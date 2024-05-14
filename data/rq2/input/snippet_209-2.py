import pandas as pd
import numpy as np
print('Original DataFrame:')
print(df)
index = df['weight'].index[df['weight'].apply(np.isnan)]
df_index = df.index.values.tolist()
print("\nInteger index of rows with missing data in 'weight' column of the said dataframe:")
print([df_index.index(i) for i in index])