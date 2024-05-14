# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1796180/how-can-i-get-a-list-of-all-classes-within-current-module-in-python
#foo.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(1543185)

except ImportError:
    pass

class Foo(_n_(1543186, "object", lambda: object)):
    _l_(1543188)

    pass
    _l_(1543187)

def print_classes():
    _l_(1543209)

    current_module = _a_(1543190, _n_(1543189, "sys", lambda: sys), "modules")[_n_(1543191, "__name__", lambda: __name__)]
    _l_(1543192)
    for key in _c_(1543195, _n_(1543193, "dir", lambda: dir), _n_(1543194, "current_module", lambda: current_module)):
        _l_(1543208)

        if _c_(1543202, _n_(1543196, "isinstance", lambda: isinstance), _c_(1543200, _n_(1543197, "getattr", lambda: getattr), _n_(1543198, "current_module", lambda: current_module), _n_(1543199, "key", lambda: key)), _n_(1543201, "type", lambda: type) ):
            _l_(1543207)

            _c_(1543205, _n_(1543203, "print", lambda: print), _n_(1543204, "key", lambda: key))
            _l_(1543206)
try:
    import foo
    _l_(1543211)

except ImportError:
    pass
_c_(1543214, _a_(1543213, _n_(1543212, "foo", lambda: foo), "print_classes"))
_l_(1543215)

