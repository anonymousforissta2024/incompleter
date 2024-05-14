#Source: https://stackoverflow.com/questions/65795814/dask-series-mean-compute-results-in-typeerror-sum-got-an-unexpected-ke
import pandas as pd 
import numpy as np
from dask import dataframe as dd

df = pd.DataFrame({'foo': [[1,2,3], [4,5,6]]})
ddf = dd.from_pandas(df, npartitions=2) 