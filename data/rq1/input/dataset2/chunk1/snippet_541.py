#Source: https://stackoverflow.com/questions/54287042/why-this-case-pandas-dataframe-assign-raise-typeerror
from math import sqrt
import pandas as pd
df = pd.DataFrame({'x':[1,2,3], 'y':[4,5,6]})

df = df.assign(d = lambda z: sqrt(z.x**2 + z.y**2))