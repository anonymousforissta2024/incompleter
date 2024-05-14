# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/773/how-do-i-use-itertools-groupby
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for x in _c_(1545323, _n_(1545318, "list", lambda: list), _c_(1545322, _n_(1545319, "groupby", lambda: groupby), _c_(1545321, _n_(1545320, "range", lambda: range), 10))):
    _l_(1545330)

    _c_(1545328, _n_(1545324, "print", lambda: print), _c_(1545327, _n_(1545325, "list", lambda: list), _n_(1545326, "x", lambda: x)[1]))
    _l_(1545329)

[]
_l_(1545331)
[]
_l_(1545332)
[]
_l_(1545333)
[]
_l_(1545334)
[]
_l_(1545335)
[]
_l_(1545336)
[]
_l_(1545337)
[]
_l_(1545338)
[]
_l_(1545339)
[9]
_l_(1545340)

def groupbylist(*args, **kwargs):
    _l_(1545350)

    aux = [(_n_(1545341, "k", lambda: k), _c_(1545344, _n_(1545342, "list", lambda: list), _n_(1545343, "g", lambda: g))) for k, g in _c_(1545348, _n_(1545345, "groupby", lambda: groupby), *_n_(1545346, "args", lambda: args), **_n_(1545347, "kwargs", lambda: kwargs))]
    _l_(1545349)
    return aux

