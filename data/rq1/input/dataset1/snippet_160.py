# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3940128/how-do-i-reverse-a-list-or-loop-over-it-backwards
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def reverse(seq):
    _l_(1541734)

    for x in _c_(1541729, _n_(1541725, "range", lambda: range), _c_(1541728, _n_(1541726, "len", lambda: len), _n_(1541727, "seq", lambda: seq)), -1, -1):
        _l_(1541733)

        yield _n_(1541730, "seq", lambda: seq)[_n_(1541731, "x", lambda: x)] #Yield a value to the generator
        _l_(1541732) #Yield a value to the generator

for x in _c_(1541736, _n_(1541735, "reverse", lambda: reverse), [1, 2, 3]):
    _l_(1541741)

    _c_(1541739, _n_(1541737, "print", lambda: print), _n_(1541738, "x", lambda: x))
    _l_(1541740)

l = _c_(1541745, _n_(1541742, "list", lambda: list), _c_(1541744, _n_(1541743, "reverse", lambda: reverse), [1, 2, 3]))
_l_(1541746)

