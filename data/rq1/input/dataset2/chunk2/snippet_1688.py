#Source: https://stackoverflow.com/questions/59313922/the-typeerror-float-object-cannot-be-interpreted-as-an-integer-in-stride-tric
import numpy as np
n=4
m=5
a = np.arange(1,n*m+1).reshape(n,m)

sz = a.itemsize
h,w = a.shape
bh,bw = 2,2
shape = (h/bh, w/bw, bh, bw)

strides = sz*np.array([w*bh,bw,w,1])


blocks=np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)
print(blocks)