#Source: https://stackoverflow.com/questions/46209731/typeerror-strptime-argument-1-must-be-str-not-float
import numpy as np
import pandas as pd
from datetime import datetime as dt

data0 = pd.read_csv('2009-10.csv')
data1 = pd.read_csv('2010-11.csv')

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%d/%m/%y').date()

data0.Date = data0.Date.apply(parse_date)
data1.Date = data1.Date.apply(parse_date)