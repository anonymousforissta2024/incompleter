# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(1539050, "somelist", lambda: somelist)[:] = _c_(1539056, _n_(1539051, "filter", lambda: filter), lambda tup: not _c_(1539054, _n_(1539052, "determine", lambda: determine), _n_(1539053, "tup", lambda: tup)), _n_(1539055, "somelist", lambda: somelist))
_l_(1539057)
try:
    from itertools import ifilterfalse
    _l_(1539059)

except ImportError:
    pass
_n_(1539060, "somelist", lambda: somelist)[:] = _c_(1539066, _n_(1539061, "list", lambda: list), _c_(1539065, _n_(1539062, "ifilterfalse", lambda: ifilterfalse), _n_(1539063, "determine", lambda: determine), _n_(1539064, "somelist", lambda: somelist)))
_l_(1539067)

