#Source: https://stackoverflow.com/questions/65795814/dask-series-mean-compute-results-in-typeerror-sum-got-an-unexpected-ke
In[3]: ddf['foo'].apply(np.float64, meta=('foo','f8')).mean().compute()