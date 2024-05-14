# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/574730/python-how-to-ignore-an-exception-and-proceed
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    _l_(1540899)

    _c_(1540894, _n_(1540893, "do_something", lambda: do_something))
    _l_(1540895)
except _n_(1540896, "Exception", lambda: Exception):
    _l_(1540898)

    pass
    _l_(1540897)

try:
    _l_(1540909)

    _c_(1540901, _n_(1540900, "do_something", lambda: do_something))
    _l_(1540902)
except _n_(1540903, "Exception", lambda: Exception):
    _l_(1540908)

    _c_(1540906, _a_(1540905, _n_(1540904, "sys", lambda: sys), "exc_clear"))
    _l_(1540907)

