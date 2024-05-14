# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8213522/when-to-use-cla-clf-or-close-for-clearing-a-plot-in-matplotlib
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for i in _c_(1546908, _n_(1546907, "range", lambda: range), 5):
    _l_(1546917)

    fig = _c_(1546910, _n_(1546909, "plot_figure", lambda: plot_figure))
    _l_(1546911)
    _c_(1546915, _a_(1546913, _n_(1546912, "plt", lambda: plt), "close"), _n_(1546914, "fig", lambda: fig))
    _l_(1546916)
# This returns a list with all figure numbers available
_c_(1546922, _n_(1546918, "print", lambda: print), _c_(1546921, _a_(1546920, _n_(1546919, "plt", lambda: plt), "get_fignums")))
_l_(1546923)

for i in _c_(1546925, _n_(1546924, "range", lambda: range), 5):
    _l_(1546933)

    fig = _c_(1546927, _n_(1546926, "plot_figure", lambda: plot_figure))
    _l_(1546928)
    _c_(1546931, _a_(1546930, _n_(1546929, "fig", lambda: fig), "clf"))
    _l_(1546932)
# This returns a list with all figure numbers available
_c_(1546938, _n_(1546934, "print", lambda: print), _c_(1546937, _a_(1546936, _n_(1546935, "plt", lambda: plt), "get_fignums")))
_l_(1546939)
try:
    import numpy as np
    _l_(1546941)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(1546943)

except ImportError:
    pass
x = _c_(1546946, _a_(1546945, _n_(1546944, "np", lambda: np), "arange"), 1000)
_l_(1546947)
y = _c_(1546951, _a_(1546949, _n_(1546948, "np", lambda: np), "sin"), _n_(1546950, "x", lambda: x))
_l_(1546952)

for i in _c_(1546954, _n_(1546953, "range", lambda: range), 5):
    _l_(1546974)

    fig = _c_(1546957, _a_(1546956, _n_(1546955, "plt", lambda: plt), "figure"))
    _l_(1546958)
    ax = _c_(1546961, _a_(1546960, _n_(1546959, "fig", lambda: fig), "add_subplot"), 1, 1, 1)
    _l_(1546962)
    _c_(1546967, _a_(1546964, _n_(1546963, "ax", lambda: ax), "plot"), _n_(1546965, "x", lambda: x), _n_(1546966, "y", lambda: y))
    _l_(1546968)
    _c_(1546972, _a_(1546970, _n_(1546969, "plt", lambda: plt), "close"), _n_(1546971, "fig", lambda: fig))
    _l_(1546973)

_c_(1546979, _n_(1546975, "print", lambda: print), _c_(1546978, _a_(1546977, _n_(1546976, "plt", lambda: plt), "get_fignums")))
_l_(1546980)

for i in _c_(1546982, _n_(1546981, "range", lambda: range), 5):
    _l_(1547001)

    fig = _c_(1546985, _a_(1546984, _n_(1546983, "plt", lambda: plt), "figure"))
    _l_(1546986)
    ax = _c_(1546989, _a_(1546988, _n_(1546987, "fig", lambda: fig), "add_subplot"), 1, 1, 1)
    _l_(1546990)
    _c_(1546995, _a_(1546992, _n_(1546991, "ax", lambda: ax), "plot"), _n_(1546993, "x", lambda: x), _n_(1546994, "y", lambda: y))
    _l_(1546996)
    _c_(1546999, _a_(1546998, _n_(1546997, "fig", lambda: fig), "clf"))
    _l_(1547000)

_c_(1547006, _n_(1547002, "print", lambda: print), _c_(1547005, _a_(1547004, _n_(1547003, "plt", lambda: plt), "get_fignums")))
_l_(1547007)

