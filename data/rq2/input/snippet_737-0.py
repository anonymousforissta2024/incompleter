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

def highlight_max(s):
    """
    highlight the maximum in a Series green.
    """
    is_max = s == s.max()
    return ['background-color: green' if v else '' for v in is_max]
print('\nHighlight the maximum value in each column:')
df.style.apply(highlight_max, subset=pd.IndexSlice[:, ['B', 'C', 'D', 'E']])