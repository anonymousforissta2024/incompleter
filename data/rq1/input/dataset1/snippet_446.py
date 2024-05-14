# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7023052/configure-flask-dev-server-to-be-visible-across-the-network
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1542909)

except ImportError:
    pass

if _n_(1542910, "__name__", lambda: __name__) == "__main__":
    _l_(1542923)

    port = _c_(1542916, _n_(1542911, "int", lambda: int), _c_(1542915, _a_(1542914, _a_(1542913, _n_(1542912, "os", lambda: os), "environ"), "get"), "PORT", 5000))
    _l_(1542917)
    _c_(1542921, _a_(1542919, _n_(1542918, "app", lambda: app), "run"), host='0.0.0.0', port=_n_(1542920, "port", lambda: port))
    _l_(1542922)

