# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/14432557/scatter-plot-with-different-text-at-each-data-point
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(1541681)

except ImportError:
    pass
y = [2.56422, 3.77284, 3.52623, 3.51468, 3.02199]
_l_(1541682)
z = [0.15, 0.3, 0.45, 0.6, 0.75]
_l_(1541683)
n = [58, 651, 393, 203, 123]
_l_(1541684)

fig, ax = _c_(1541689, _a_(1541686, _n_(1541685, "plt", lambda: plt), "scatter"), _n_(1541687, "z", lambda: z), _n_(1541688, "y", lambda: y))
_l_(1541690)

for i, txt in _c_(1541693, _n_(1541691, "enumerate", lambda: enumerate), _n_(1541692, "n", lambda: n)):
    _l_(1541703)

    _c_(1541701, _a_(1541695, _n_(1541694, "ax", lambda: ax), "annotate"), _n_(1541696, "txt", lambda: txt), (_n_(1541697, "z", lambda: z)[_n_(1541698, "i", lambda: i)], _n_(1541699, "y", lambda: y)[_n_(1541700, "i", lambda: i)]))
    _l_(1541702)
try:
    import matplotlib.pyplot as plt
    _l_(1541705)

except ImportError:
    pass
_c_(1541710, _a_(1541707, _n_(1541706, "plt", lambda: plt), "scatter"), _n_(1541708, "z", lambda: z), _n_(1541709, "y", lambda: y))
_l_(1541711)

for i, txt in _c_(1541714, _n_(1541712, "enumerate", lambda: enumerate), _n_(1541713, "n", lambda: n)):
    _l_(1541724)

    _c_(1541722, _a_(1541716, _n_(1541715, "plt", lambda: plt), "annotate"), _n_(1541717, "txt", lambda: txt), (_n_(1541718, "z", lambda: z)[_n_(1541719, "i", lambda: i)], _n_(1541720, "y", lambda: y)[_n_(1541721, "i", lambda: i)]))
    _l_(1541723)

