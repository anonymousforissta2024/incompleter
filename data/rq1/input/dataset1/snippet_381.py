# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9252543/what-can-i-do-about-importerror-cannot-import-name-x-or-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from test.b import b2
    _l_(1547077)

except ImportError:
    pass

def a1():
    _l_(1547084)

    _c_(1547079, _n_(1547078, "print", lambda: print), 'a1')
    _l_(1547080)
    _c_(1547082, _n_(1547081, "b2", lambda: b2))
    _l_(1547083)
try:
    from test.a import a1
    _l_(1547086)

except ImportError:
    pass

def b1():
    _l_(1547093)

    _c_(1547088, _n_(1547087, "print", lambda: print), 'b1')
    _l_(1547089)
    _c_(1547091, _n_(1547090, "a1", lambda: a1))
    _l_(1547092)

def b2():
    _l_(1547097)

    _c_(1547095, _n_(1547094, "print", lambda: print), 'b2')
    _l_(1547096)

if _n_(1547098, "__name__", lambda: __name__) == '__main__':
    _l_(1547102)

    _c_(1547100, _n_(1547099, "b1", lambda: b1))
    _l_(1547101)

def a1():
    _l_(1547109)

    _c_(1547104, _n_(1547103, "print", lambda: print), 'a1')
    _l_(1547105)
    _c_(1547107, _n_(1547106, "b2", lambda: b2))
    _l_(1547108)
try:
    from test.b import b2
    _l_(1547111)

except ImportError:
    pass

_n_(1547112, "b1", lambda: b1)
_l_(1547113)
_n_(1547114, "a1", lambda: a1)
_l_(1547115)
_n_(1547116, "b2", lambda: b2)
_l_(1547117)

