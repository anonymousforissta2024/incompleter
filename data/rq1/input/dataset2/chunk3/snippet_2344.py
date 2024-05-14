#Source: https://stackoverflow.com/questions/58800137/rpy2-typeerror-parameter-categories-must-be-list-like
# Convert R Dataframe to python Dataframe
# !pip install tzlocal
# type(data)
from rpy2.robjects import pandas2ri
pd_df = pandas2ri.ri2py_dataframe(data)
pd_df