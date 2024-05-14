#Source: https://stackoverflow.com/questions/55540107/how-to-fix-attributeerror-function-object-has-no-attribute-rcparams
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv', index_col='time')
df.sort_values(by='time')

plt.plot(df['ecg'], label='data', color="orange")

plt.plot.rcParams['agg.path.chunksize'] = 20000


plt.title("ECG Data")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()