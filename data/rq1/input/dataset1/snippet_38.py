# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/739654/how-do-i-make-function-decorators-and-chain-them-together
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_n_(1547552, "decorator", lambda: decorator)
def func():
    _l_(1547554)

    ...
    _l_(1547553)

def func():
    _l_(1547556)

    ...
    _l_(1547555)
func = _c_(1547559, _n_(1547557, "decorator", lambda: decorator), _n_(1547558, "func", lambda: func))
_l_(1547560)

