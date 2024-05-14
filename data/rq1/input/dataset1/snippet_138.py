# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/192109/is-there-a-built-in-function-to-print-all-the-current-properties-and-values-of-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pprint import pprint
    _l_(1548353)

except ImportError:
    pass
_c_(1548358, _n_(1548354, "pprint", lambda: pprint), _c_(1548357, _n_(1548355, "vars", lambda: vars), _n_(1548356, "your_object", lambda: your_object)))
_l_(1548359)

