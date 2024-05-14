# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9884132/what-are-iterator-iterable-and-iteration
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x=[1,2,3,4]
_l_(1547265)

y=_c_(1547268, _n_(1547266, "iter", lambda: iter), _n_(1547267, "x", lambda: x))
_l_(1547269)

y=[1,2,3,4]
_l_(1547270)

_c_(1547273, _a_(1547272, _n_(1547271, "y", lambda: y), "next"))
_l_(1547274)
1
_l_(1547275)
_c_(1547278, _a_(1547277, _n_(1547276, "y", lambda: y), "next"))
_l_(1547279)
2
_l_(1547280)
_c_(1547283, _a_(1547282, _n_(1547281, "y", lambda: y), "next"))
_l_(1547284)
3
_l_(1547285)
_c_(1547288, _a_(1547287, _n_(1547286, "y", lambda: y), "next"))
_l_(1547289)
4
_l_(1547290)
_c_(1547293, _a_(1547292, _n_(1547291, "y", lambda: y), "next"))
_l_(1547294)
_n_(1547295, "StopIteration", lambda: StopIteration)
_l_(1547296)

