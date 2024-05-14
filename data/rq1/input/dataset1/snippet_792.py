# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/17534345/typeerror-missing-1-required-positional-argument-self
# WRONG! will result in TypeError: getPumps() missing 1 required positional argument: 'self'
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
p = _n_(1540976, "Pump", lambda: Pump)
_l_(1540977)
_c_(1540980, _a_(1540979, _n_(1540978, "p", lambda: p), "getPumps"))
_l_(1540981)

# CORRECT!
p = _c_(1540983, _n_(1540982, "Pump", lambda: Pump))
_l_(1540984)
_c_(1540987, _a_(1540986, _n_(1540985, "p", lambda: p), "getPumps"))
_l_(1540988)

