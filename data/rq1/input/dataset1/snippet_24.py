# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/448271/what-is-init-py-for
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1547767)

except ImportError:
    pass
try:
    import sys
    _l_(1547769)

except ImportError:
    pass
dir_path = _c_(1547774, _a_(1547772, _a_(1547771, _n_(1547770, "os", lambda: os), "path"), "dirname"), _n_(1547773, "__file__", lambda: __file__))
_l_(1547775)
_c_(1547780, _a_(1547778, _a_(1547777, _n_(1547776, "sys", lambda: sys), "path"), "insert"), 0, _n_(1547779, "dir_path", lambda: dir_path))
_l_(1547781)
try:
    import cheese
    _l_(1547783)

except ImportError:
    pass
try:
    from vehicle_parts import *
    _l_(1547785)

except ImportError:
    pass
# etc.

