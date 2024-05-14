#Source: https://stackoverflow.com/questions/59915199/error-nameerror-name-json-is-not-defined
from json import *
import pandas as pd
import numpy as np
import os

fp=open("data1.json","r")
data=json.loads(fp)
print(data)

s=pd.Series(data,index=[1,2])
print(s)