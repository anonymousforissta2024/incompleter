#Source: https://stackoverflow.com/questions/74642934/how-to-resolve-attribute-error-array-array-object-has-no-attribute-read-in-py
import os
from functools import reduce
import numpy
import array
from utils import *

def load_raw_data_with_mhd(filename):
    meta_dict = read_meta_header(filename)
    dim = int(meta_dict['NDims'])
    assert(meta_dict['ElementType']=='MET_FLOAT')
    arr = [int(i) for i in meta_dict['DimSize'].split()]
    volume = reduce(lambda x,y: x*y, arr[0:dim-1], 1)
    pwd = os.path.split(filename)[0]
    if pwd:
        data_file = pwd +'/' + meta_dict['ElementDataFile']
    else:
        data_file = meta_dict['ElementDataFile']
    print (data_file)
    fid = open(data_file,'rb')
    binvalues = array.array('f')
    binvalues.read(fid, volume*arr[dim-1])
    if is_little_endian(): # assume data in file is always big endian
        binvalues.byteswap()
    fid.close()
    data = numpy.array(binvalues, numpy.float)
    data = numpy.reshape(data, (arr[dim-1], volume))
    return (data, meta_dict)