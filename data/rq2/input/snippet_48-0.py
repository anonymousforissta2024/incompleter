import pandas as pd
import numpy as np
import seaborn as sns
np.random.seed(24)
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))], axis=1)
print('Original array:')
print(df)
print('\nDataframe - Gradient color:')
df.style.background_gradient()