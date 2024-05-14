# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/423379/using-global-variables-in-a-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def five(enterAnumber,sumation):
    _l_(1547790)

    global helper
    _l_(1547786)
    helper  = _n_(1547787, "enterAnumber", lambda: enterAnumber) + _n_(1547788, "sumation", lambda: sumation)
    _l_(1547789)

def isTheNumber():
    _l_(1547793)

    aux = _n_(1547791, "helper", lambda: helper)
    _l_(1547792)
    return aux
try:
    import TestPy
    _l_(1547795)

except ImportError:
    pass

def main():
    _l_(1547808)

    atest  = _n_(1547796, "TestPy", lambda: TestPy)
    _l_(1547797)
    _c_(1547800, _a_(1547799, _n_(1547798, "atest", lambda: atest), "five"), 5,8)
    _l_(1547801)
    _c_(1547806, _n_(1547802, "print", lambda: print), _c_(1547805, _a_(1547804, _n_(1547803, "atest", lambda: atest), "isTheNumber")))
    _l_(1547807)

if _n_(1547809, "__name__", lambda: __name__) == '__main__':
    _l_(1547813)

    _c_(1547811, _n_(1547810, "main", lambda: main))
    _l_(1547812)

