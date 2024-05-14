import numpy as np
import pandas as pd
print('Original Numpy array:')
print(np_array)
print('Type: ', type(np_array))
df = pd.DataFrame(np.random.rand(12, 3), columns=['A', 'B', 'C'])
print("\nPanda's DataFrame: ")
print(df)
print('Type: ', type(df))