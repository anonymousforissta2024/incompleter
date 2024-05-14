# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import six
    _l_(1538261)

except ImportError:
    pass

if _c_(1538266, _n_(1538262, "isinstance", lambda: isinstance), _n_(1538263, "value", lambda: value), _a_(1538265, _n_(1538264, "six", lambda: six), "string_types")):
    _l_(1538268)

    pass # It's a string !!
    _l_(1538267) # It's a string !!
try:
    import sys
    _l_(1538270)

except ImportError:
    pass

PY3 = _a_(1538272, _n_(1538271, "sys", lambda: sys), "version_info")[0] == 3
_l_(1538273)

if _n_(1538274, "PY3", lambda: PY3):
    _l_(1538279)

    string_types = _n_(1538275, "str", lambda: str),
    _l_(1538276)
else:
    string_types = _n_(1538277, "basestring", lambda: basestring),
    _l_(1538278)

