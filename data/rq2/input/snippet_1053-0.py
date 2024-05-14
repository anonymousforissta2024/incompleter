import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.DataFrame({'student_id': ['S001', 'S001', 'S002', 'S002', 'S003', 'S003'], 'marks': [[88, 89, 90], [78, 81, 60], [84, 83, 91], [84, 88, 91], [90, 89, 92], [88, 59, 90]]})
print('Original DataFrame:')
print(df)
print('\nGroupby and aggregate over multiple lists:')
print(result)