# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/993984/what-are-the-advantages-of-numpy-over-regular-python-lists
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = _c_(1543891, _a_(1543890, _c_(1543889, _a_(1543885, _n_(1543884, "numpy", lambda: numpy), "fromfile"), file=_c_(1543887, _n_(1543886, "open", lambda: open), "data"), dtype=_n_(1543888, "float", lambda: float)), "reshape"), (100, 100, 100))
_l_(1543892)

s = _c_(1543895, _a_(1543894, _n_(1543893, "x", lambda: x), "sum"), axis=1)
_l_(1543896)

_c_(1543899, _a_(1543898, (_n_(1543897, "x", lambda: x) > 0.5), "nonzero"))
_l_(1543900)

_n_(1543901, "x", lambda: x)[:, :, ::2]
_l_(1543902)

