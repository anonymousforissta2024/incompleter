#Source: https://stackoverflow.com/questions/52242859/file-e-python-lib-re-py-line-229-in-finditer-return-compilepattern-flags
from skimage.feature import greycomatrix
import numpy as np 

image=np.array([[1,1,5,6,8],
                [0,0,5,7,1],
                [4,0,0,1,2],
                [8,5,1,2,5]],dtype=np.uint8)
#levels=256   image   this test is 9
result=greycomatrix(image,[1],[0,np.pi/4,np.pi/2,3*np.pi/4],levels=9)
print(result[:, :, 0, 0])