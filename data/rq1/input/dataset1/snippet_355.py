# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
10 
_l_(1541814) 
10
_l_(1541815)

_n_(1541816, "_", lambda: _) 
_l_(1541817) 
10
_l_(1541818)

_n_(1541819, "_", lambda: _) * 3 
_l_(1541820) 
30
_l_(1541821)

x, _, y = (1, 2, 3)
_l_(1541822)

_n_(1541823, "x", lambda: x)
_l_(1541824)
1
_l_(1541825)

_n_(1541826, "y", lambda: y) 
_l_(1541827) 
3
_l_(1541828)

for _ in _c_(1541830, _n_(1541829, "range", lambda: range), 10):
    _l_(1541834)

    _c_(1541832, _n_(1541831, "do_something", lambda: do_something))
    _l_(1541833)

