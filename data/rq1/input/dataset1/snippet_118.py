# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/230751/how-can-i-flush-the-output-of-the-print-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
f = _c_(1548159, _n_(1548158, "open", lambda: open), 'xyz.log', 'a', 0)
_l_(1548160)

_n_(1548161, "sys", lambda: sys).stdout = _c_(1548163, _n_(1548162, "open", lambda: open), 'out.log', 'a', 0)
_l_(1548164)

