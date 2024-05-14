# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10580676/comparing-two-numpy-arrays-for-equality-element-wise
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(1544853)

except ImportError:
    pass
a = _c_(1544856, _a_(1544855, _n_(1544854, "np", lambda: np), "arange"), 0.0, 10.2, 0.12)
_l_(1544857)
b = _c_(1544860, _a_(1544859, _n_(1544858, "np", lambda: np), "arange"), 0.0, 10.2, 0.12)
_l_(1544861)
ap = _c_(1544865, _a_(1544863, _n_(1544862, "pd", lambda: pd), "DataFrame"), _n_(1544864, "a", lambda: a))
_l_(1544866)
bp = _c_(1544870, _a_(1544868, _n_(1544867, "pd", lambda: pd), "DataFrame"), _n_(1544869, "b", lambda: b))
_l_(1544871)

_c_(1544875, _a_(1544873, _n_(1544872, "ap", lambda: ap), "equals"), _n_(1544874, "bp", lambda: bp))
_l_(1544876)
True
_l_(1544877)

_c_(1544881, _n_(1544878, "identical", lambda: identical), _n_(1544879, "iris1", lambda: iris1), _n_(1544880, "iris2", lambda: iris2))
_l_(1544882)
#[1] TRUE
_c_(1544887, _a_(1544884, _n_(1544883, "all", lambda: all), "equal"), _n_(1544885, "array1", lambda: array1), _n_(1544886, "array2", lambda: array2))
_l_(1544888)
#> [1] TRUE 

