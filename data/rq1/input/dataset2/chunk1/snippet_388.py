#Source: https://stackoverflow.com/questions/75580189/filter-none-value-from-python-list-returns-typeerror-boolean-value-of-na-is-am
import pandas as pd
x = pd.array(['This is', 'some text', None, 'data.'], dtype="string")
x = list(x.unique())
list(filter(None, x))