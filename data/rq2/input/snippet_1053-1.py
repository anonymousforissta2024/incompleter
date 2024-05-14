import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print('Original DataFrame:')
print(df)
print('\nGroupby and aggregate over multiple lists:')
result = df.set_index('student_id')['marks'].groupby('student_id').apply(list).apply(lambda x: np.mean(x, 0))
print(result)