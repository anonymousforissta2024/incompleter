# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from typeguard import check_type
    _l_(1548396)

except ImportError:
    pass
try:
    from typing import List
    _l_(1548398)

except ImportError:
    pass

try:
    _l_(1548410)

    _c_(1548402, _n_(1548399, "check_type", lambda: check_type), 'mylist', [1, 2], _n_(1548400, "List", lambda: List)[_n_(1548401, "int", lambda: int)])
    _l_(1548403)
except _n_(1548404, "TypeError", lambda: TypeError) as e:
    _l_(1548409)

    _c_(1548407, _n_(1548405, "print", lambda: print), _n_(1548406, "e", lambda: e))
    _l_(1548408)

_c_(1548416, _n_(1548411, "check_type", lambda: check_type), 'foo', [1, 3.14], _n_(1548412, "List", lambda: List)[_n_(1548413, "Union", lambda: Union)[_n_(1548414, "int", lambda: int), _n_(1548415, "float", lambda: float)]])
_l_(1548417)
# vs
_c_(1548421, _n_(1548418, "isinstance", lambda: isinstance), _n_(1548419, "foo", lambda: foo), _n_(1548420, "list", lambda: list)) and _c_(1548429, _n_(1548422, "all", lambda: all), (_c_(1548427, _n_(1548423, "isinstance", lambda: isinstance), _n_(1548424, "a", lambda: a), (_n_(1548425, "int", lambda: int), _n_(1548426, "float", lambda: float))) for a in _n_(1548428, "foo", lambda: foo))) 
_l_(1548430) 

