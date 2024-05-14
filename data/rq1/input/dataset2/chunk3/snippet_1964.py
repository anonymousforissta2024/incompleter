#Source: https://stackoverflow.com/questions/65795814/dask-series-mean-compute-results-in-typeerror-sum-got-an-unexpected-ke
In[1]: df['foo'].apply(np.float64).mean()
Out[1]: array([2.5, 3.5, 4.5])