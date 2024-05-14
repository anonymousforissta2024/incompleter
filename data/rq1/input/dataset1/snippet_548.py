# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1316767/how-can-i-explicitly-free-memory-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from dask import delayed
    _l_(1541653)

except ImportError:
    pass
def f(storage, index, chunk_size):
    _l_(1541656)

    aux = _n_(1541654, "storage", lambda: storage)
    _l_(1541655)
    # read the chunk of size chunk_size starting at index in the file
    # process it using data in storage if needed
    # append data needed for further computations  to storage 
    return aux

partial_result = _c_(1541658, _n_(1541657, "delayed", lambda: delayed), [])  # put into the delayed() the constructor for your data structure
_l_(1541659)  # put into the delayed() the constructor for your data structure
# I personally use "delayed(nx.Graph())" since I am creating a networkx Graph
chunk_size = 100  # ideally you want this as big as possible while still enabling the computations to fit in memory
_l_(1541660)  # ideally you want this as big as possible while still enabling the computations to fit in memory
for index in _c_(1541666, _n_(1541661, "range", lambda: range), 0, _c_(1541664, _n_(1541662, "len", lambda: len), _n_(1541663, "file", lambda: file)), _n_(1541665, "chunk_size", lambda: chunk_size)):
    _l_(1541675)

    # we indicates to dask that we will want to apply f to the parameters partial_result, index, chunk_size
    partial_result = _c_(1541673, _c_(1541669, _n_(1541667, "delayed", lambda: delayed), _n_(1541668, "f", lambda: f)), _n_(1541670, "partial_result", lambda: partial_result), _n_(1541671, "index", lambda: index), _n_(1541672, "chunk_size", lambda: chunk_size))
    _l_(1541674)

# this launches all the computations
result = _c_(1541678, _a_(1541677, _n_(1541676, "partial_result", lambda: partial_result), "compute"))
_l_(1541679)

# one thread is spawned for each "delayed" one at a time to compute its result
# dask then closes the tread, which solves the memory freeing issue
# the strange performance issue with gc.collect() is also avoided

