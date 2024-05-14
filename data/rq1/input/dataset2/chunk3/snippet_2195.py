#Source: https://stackoverflow.com/questions/63660467/typeerror-unhashable-type-dict-unable-to-read-parquet-file-with-dask
import pyarrow
import dask.dataframe as dd

data = dd.read_parquet('myfile.parquet', engine = 'pyarrow')