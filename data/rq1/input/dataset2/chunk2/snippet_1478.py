#Source: https://stackoverflow.com/questions/57318922/typeerror-argument-x-has-incorrect-type-expected-cupy-core-core-ndarray-got
import numpy, cupy, cupyx

print( cupyx.get_runtime_info() )

mydata = numpy.empty((3,), dtype='f')

#gpu = False
gpu = True
if not gpu:
    xp = numpy
else:
    xp = cupy

    mydata_like = xp.zeros_like(mydata)