#Source: https://stackoverflow.com/questions/65998183/python-dask-module-error-attributeerror-io-textiowrapper-object-has-no-at
import dask.array as da
import dask.dataframe as ddf
'''Read .csv straight to list'''  
with open (wd+inputfilename+extension_csv, 'r') as f:
    reader = csv.reader(f)
    df = ddf.read_csv(f)   #data here is a dask pandas dataframe