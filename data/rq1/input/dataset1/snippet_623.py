# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/100210/what-is-the-standard-way-to-add-n-seconds-to-datetime-time-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(1541469)

except ImportError:
    pass
try:
    import nptime
    _l_(1541471)

except ImportError:
    pass
_c_(1541474, _a_(1541473, _n_(1541472, "nptime", lambda: nptime), "nptime"), 11, 34, 59) + _c_(1541477, _a_(1541476, _n_(1541475, "datetime", lambda: datetime), "timedelta"), 0, 3)
_l_(1541478)
_c_(1541480, _n_(1541479, "nptime", lambda: nptime), 11, 35, 2)
_l_(1541481)

