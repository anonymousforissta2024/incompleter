# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def find_nearest(array, values):
    _l_(1539741)

    array = _c_(1539723, _a_(1539721, _n_(1539720, "np", lambda: np), "asarray"), _n_(1539722, "array", lambda: array))
    _l_(1539724)

    # the last dim must be 1 to broadcast in (array - values) below.
    values = _c_(1539728, _a_(1539726, _n_(1539725, "np", lambda: np), "expand_dims"), _n_(1539727, "values", lambda: values), axis=-1) 
    _l_(1539729) 

    indices = _c_(1539736, _a_(1539735, _c_(1539734, _a_(1539731, _n_(1539730, "np", lambda: np), "abs"), _n_(1539732, "array", lambda: array) - _n_(1539733, "values", lambda: values)), "argmin"), axis=-1)
    _l_(1539737)
    aux = _n_(1539738, "array", lambda: array)[_n_(1539739, "indices", lambda: indices)]
    _l_(1539740)

    return aux


image = _c_(1539744, _a_(1539743, _n_(1539742, "plt", lambda: plt), "imread"), 'example_3_band_image.jpg')
_l_(1539745)

_c_(1539749, _n_(1539746, "print", lambda: print), _a_(1539748, _n_(1539747, "image", lambda: image), "shape")) # should be (nrows, ncols, 3)
_l_(1539750) # should be (nrows, ncols, 3)

quantiles = _c_(1539755, _a_(1539752, _n_(1539751, "np", lambda: np), "linspace"), 0, 255, num=2 ** 2, dtype=_a_(1539754, _n_(1539753, "np", lambda: np), "uint8"))
_l_(1539756)

quantiled_image = _c_(1539760, _n_(1539757, "find_nearest", lambda: find_nearest), _n_(1539758, "quantiles", lambda: quantiles), _n_(1539759, "image", lambda: image))
_l_(1539761)

_c_(1539765, _n_(1539762, "print", lambda: print), _a_(1539764, _n_(1539763, "quantiled_image", lambda: quantiled_image), "shape")) # should be (nrows, ncols, 3)
_l_(1539766) # should be (nrows, ncols, 3)

