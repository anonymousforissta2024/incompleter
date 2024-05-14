import pandas as pd
str1 = 'abc def abcdef icd'
print('Original series:')
print(str1)
ser = pd.Series(list(str1))
print(element_freq)
current_freq = element_freq.dropna().index[-1]
result = ''.join(ser.replace(' ', current_freq))
print(result)