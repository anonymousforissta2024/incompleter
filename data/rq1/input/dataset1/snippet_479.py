# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11774265/how-do-you-access-the-query-string-in-flask-routes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
date = _c_(1545281, _a_(1545280, _a_(1545279, _n_(1545278, "request", lambda: request), "args"), "get"), 'date')
_l_(1545282)
try:
    from flask import request
    _l_(1545284)

except ImportError:
    pass

