# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/34439/finding-what-methods-a-python-object-has
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import inspect
    _l_(1542319)

except ImportError:
    pass
method_names = [_n_(1542320, "attr", lambda: attr) for attr in _c_(1542323, _n_(1542321, "dir", lambda: dir), _n_(1542322, "self", lambda: self)) if _c_(1542330, _a_(1542325, _n_(1542324, "inspect", lambda: inspect), "ismethod"), _c_(1542329, _n_(1542326, "getattr", lambda: getattr), _n_(1542327, "self", lambda: self), _n_(1542328, "attr", lambda: attr)))]
_l_(1542331)
try:
    import inspect
    _l_(1542333)

except ImportError:
    pass
methods = [_n_(1542334, "member", lambda: member) for member in [_c_(1542338, _n_(1542335, "getattr", lambda: getattr), _n_(1542336, "self", lambda: self), _n_(1542337, "attr", lambda: attr)) for attr in _c_(1542341, _n_(1542339, "dir", lambda: dir), _n_(1542340, "self", lambda: self))] if _c_(1542345, _a_(1542343, _n_(1542342, "inspect", lambda: inspect), "ismethod"), _n_(1542344, "member", lambda: member))]
_l_(1542346)

