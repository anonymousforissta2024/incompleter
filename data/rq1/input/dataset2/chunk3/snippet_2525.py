#Source: https://stackoverflow.com/questions/65795814/dask-series-mean-compute-results-in-typeerror-sum-got-an-unexpected-ke
In[2]: ddf['foo'].apply(np.float64, meta=('foo','f8')).compute().mean()
Out[2]: array([2.5, 3.5, 4.5])