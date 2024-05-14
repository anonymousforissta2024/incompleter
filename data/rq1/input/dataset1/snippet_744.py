# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/34162443/why-do-many-examples-use-fig-ax-plt-subplots-in-matplotlib-pyplot-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(1540152)

except ImportError:
    pass

# global state version - modifies "current" figure
_c_(1540155, _a_(1540154, _n_(1540153, "plt", lambda: plt), "plot"), ...)
_l_(1540156)
_c_(1540159, _a_(1540158, _n_(1540157, "plt", lambda: plt), "xlabel"), ...)
_l_(1540160)

# axes version - modifies explicit axes
_c_(1540163, _a_(1540162, _n_(1540161, "ax", lambda: ax), "plot"), ...)
_l_(1540164)
_c_(1540167, _a_(1540166, _n_(1540165, "ax", lambda: ax), "set_xlabel"), ...)
_l_(1540168)

