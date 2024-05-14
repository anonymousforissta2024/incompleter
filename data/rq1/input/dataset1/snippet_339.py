# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10458437/what-is-the-difference-between-dict-items-and-dict-iteritems-in-python2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
dict = {_n_(1543453, "i", lambda: i): _n_(1543454, "i", lambda: i) * 2 for i in _c_(1543456, _n_(1543455, "xrange", lambda: xrange), 10000000)}  
_l_(1543457)  
# Slow and memory hungry.
for key, value in _c_(1543460, _a_(1543459, _n_(1543458, "dict", lambda: dict), "items")):
    _l_(1543466)

    _c_(1543464, _n_(1543461, "print", lambda: print), _n_(1543462, "key", lambda: key),":",_n_(1543463, "value", lambda: value))
    _l_(1543465)

dict = {_n_(1543467, "i", lambda: i): _n_(1543468, "i", lambda: i) * 2 for i in _c_(1543470, _n_(1543469, "xrange", lambda: xrange), 10000000)}  
_l_(1543471)  
# More memory efficient.
for key, value in _c_(1543474, _a_(1543473, _n_(1543472, "dict", lambda: dict), "iteritems")):
    _l_(1543480)

    _c_(1543478, _n_(1543475, "print", lambda: print), _n_(1543476, "key", lambda: key),":",_n_(1543477, "value", lambda: value))
    _l_(1543479)

