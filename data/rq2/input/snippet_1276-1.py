import pandas as pd
import numpy as np
np.random.seed(24)
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))], axis=1)
df.iloc[0, 2] = np.nan
df.iloc[3, 3] = np.nan
df.iloc[4, 1] = np.nan
df.iloc[9, 4] = np.nan
print('Original array:')
print(df)
print('\nDifferent background color:')
coldict = {'B': 'red', 'D': 'yellow'}

def highlight_cols(x):
    df = x.copy()
    df.loc[:, :] = 'background-color: red'
    df[['B', 'C', 'E']] = 'background-color: grey'
    return df
df.style.apply(highlight_cols, axis=None)