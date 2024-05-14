import pandas as pd
print('Original Series:')
print(series1)
print('\nDifference of differences between consecutive numbers of the said series:')
print(series1.diff().tolist())
print(series1.diff().diff().tolist())