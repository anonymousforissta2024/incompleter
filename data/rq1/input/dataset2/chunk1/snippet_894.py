#Source: https://stackoverflow.com/questions/75126511/sklearn-with-joblib-raises-attributeerror-nonetype-object-has-no-attribute
import numpy as np
from joblib import Parallel, delayed, parallel_backend
from sklearn.neighbors import NearestNeighbors


def it():    
    df = np.random.randn(1000).reshape(-1,1)
    NearestNeighbors(n_neighbors=2, p=2).fit(df).kneighbors(df)
    yield 1

f = lambda x: 1
with parallel_backend("loky", inner_max_num_threads=1):
    res = Parallel(n_jobs=2)(delayed(f)(p) for p in  it())