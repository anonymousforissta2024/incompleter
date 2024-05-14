# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4888027/python-and-pip-list-all-versions-of-a-package-thats-available
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(1538458)

except ImportError:
    pass
r = _c_(1538461, _a_(1538460, _n_(1538459, "requests", lambda: requests), "get"), "https://pypi.org/pypi/Flask/json")
_l_(1538462)
_c_(1538469, _n_(1538463, "print", lambda: print), _c_(1538468, _a_(1538467, _c_(1538466, _a_(1538465, _n_(1538464, "r", lambda: r), "json"))['releases'], "keys")))
_l_(1538470)

_c_(1538472, _n_(1538471, "dict_keys", lambda: dict_keys), ['0.1', '0.10', '0.10.1', '0.11', '0.11.1', '0.12', '0.12.1', '0.12.2', '0.12.3', '0.12.4', '0.2', '0.3', '0.3.1', '0.4', '0.5', '0.5.1', '0.5.2', '0.6', '0.6.1', '0.7', '0.7.1', '0.7.2', '0.8', '0.8.1', '0.9', '1.0', '1.0.1', '1.0.2'])
_l_(1538473)

