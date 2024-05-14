# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/30081275/why-is-1000000000000000-in-range1000000000000001-so-fast-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
a = _c_(1547461, _n_(1547460, "range", lambda: range), 5)
_l_(1547462)
_c_(1547467, _n_(1547463, "print", lambda: print), _c_(1547466, _n_(1547464, "list", lambda: list), _n_(1547465, "a", lambda: a)))
_l_(1547468)
[0, 1, 2, 3, 4]
_l_(1547469)
_c_(1547474, _n_(1547470, "print", lambda: print), _c_(1547473, _n_(1547471, "list", lambda: list), _n_(1547472, "a", lambda: a)))
_l_(1547475)
[0, 1, 2, 3, 4]
_l_(1547476)

b = _c_(1547478, _n_(1547477, "my_crappy_range", lambda: my_crappy_range), 5)
_l_(1547479)
_c_(1547484, _n_(1547480, "print", lambda: print), _c_(1547483, _n_(1547481, "list", lambda: list), _n_(1547482, "b", lambda: b)))
_l_(1547485)
[0, 1, 2, 3, 4]
_l_(1547486)
_c_(1547491, _n_(1547487, "print", lambda: print), _c_(1547490, _n_(1547488, "list", lambda: list), _n_(1547489, "b", lambda: b)))
_l_(1547492)
[]
_l_(1547493)
try:
    import collections.abc
    _l_(1547495)

except ImportError:
    pass
_c_(1547500, _n_(1547496, "isinstance", lambda: isinstance), _n_(1547497, "a", lambda: a), _a_(1547499, _a_(1547498, collections, "abc"), "Sequence"))
_l_(1547501)
True
_l_(1547502)

_n_(1547503, "a", lambda: a)[3]         # indexable
_l_(1547504)         # indexable
3
_l_(1547505)
_c_(1547508, _n_(1547506, "len", lambda: len), _n_(1547507, "a", lambda: a))       # sized
_l_(1547509)       # sized
5
_l_(1547510)
3 in _n_(1547511, "a", lambda: a)       # membership
_l_(1547512)       # membership
True
_l_(1547513)
_c_(1547516, _n_(1547514, "reversed", lambda: reversed), _n_(1547515, "a", lambda: a))  # reversible
_l_(1547517)  # reversible
_c_(1547520, _a_(1547519, _n_(1547518, "a", lambda: a), "index"), 3)   # implements 'index'
_l_(1547521)   # implements 'index'
3
_l_(1547522)
_c_(1547525, _a_(1547524, _n_(1547523, "a", lambda: a), "count"), 3)   # implements 'count'
_l_(1547526)   # implements 'count'
1
_l_(1547527)

