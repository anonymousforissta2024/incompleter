import pandas as pd
from dateutil.parser import parse
print('Original Series:')
print(date_series)
print('\nNew dates:')
result = date_series.map(lambda d: parse('11 ' + d))
print(result)