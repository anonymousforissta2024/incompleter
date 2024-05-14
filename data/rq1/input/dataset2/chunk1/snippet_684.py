#Source: https://stackoverflow.com/questions/61723726/dask-apply-function-to-return-dataframe-attributeerror-dataframe-object-has
import pandas as pd
from dask import dataframe as dd

dummy_df = pd.DataFrame({'a' : [1,2,3,4,5]})

dd_dummy = dd.from_pandas(dummy_df, npartitions = 1)

"""Arbitrary function that returns dataframe, taking keyword argument from apply"""
def test(x, bleh):
    return pd.DataFrame({'test' : 7 * [bleh]})

ok = dd_dummy.apply(test, axis = 1
                , bleh = 'fish'
                , meta = {'test' : 'str'}).compute()