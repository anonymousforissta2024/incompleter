# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1911281/how-do-i-get-list-of-methods-in-a-python-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
methods = [(_n_(1545474, "func", lambda: func), _c_(1545478, _n_(1545475, "getattr", lambda: getattr), _n_(1545476, "o", lambda: o), _n_(1545477, "func", lambda: func))) for func in _c_(1545481, _n_(1545479, "dir", lambda: dir), _n_(1545480, "o", lambda: o)) if _c_(1545487, _n_(1545482, "callable", lambda: callable), _c_(1545486, _n_(1545483, "getattr", lambda: getattr), _n_(1545484, "o", lambda: o), _n_(1545485, "func", lambda: func)))]
_l_(1545488)

methods = _c_(1545494, _a_(1545490, _n_(1545489, "inspect", lambda: inspect), "getmembers"), _n_(1545491, "o", lambda: o), predicate=_a_(1545493, _n_(1545492, "inspect", lambda: inspect), "ismethod"))
_l_(1545495)

