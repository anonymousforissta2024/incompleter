#Source: https://stackoverflow.com/questions/37530891/python-pandas-nameerror-stringio-is-not-defined
import pandas as pd

data = 'a,b,c\n1,2,3\n4,5,6'

pd.read_csv(StringIO(data),skipinitialspace=True)