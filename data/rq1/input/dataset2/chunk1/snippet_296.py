#Source: https://stackoverflow.com/questions/60649173/numpy-typeerror-ufunc-bitwise-and-not-supported-for-the-input-types
df_merge = pd.DataFrame({'column1': ['a', 'c', 'e'],
               'column2': ['b', 'd', 'f'],
               'column3': [0.5, 0.6, .04],
               'column4': [0.7, 0.8, 0.9],
               'Reason': ['correct, should not have', 'correct, should not have', 'correct, should not have'],
               })