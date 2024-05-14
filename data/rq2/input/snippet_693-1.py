import pandas as pd
series2 = pd.Series([1, 3, 5, 7, 10])
print('Original Series:')
print(series1)
print(series2)
result = [pd.Index(series1).get_loc(i) for i in series2]
print('Positions of items of series2 in series1:')
print(result)