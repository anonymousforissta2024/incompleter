import pandas as pd
import numpy as np
np.random.seed(24)
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))], axis=1)
print('Original array:')
print(df)
print('\nDataframe - table style:')

def highlight_greaterthan(x):
    if x.C > 0.5:
        return ['background-color: yellow'] * 5
    else:
        return ['background-color: white'] * 5
df.style.apply(highlight_greaterthan, axis=1)