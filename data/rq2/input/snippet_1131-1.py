import pandas as pd
print('Original Data Series:')
print(s1)
print('Change the said data type to numeric:')
s2 = pd.to_numeric(s1, errors='coerce')
print(s2)