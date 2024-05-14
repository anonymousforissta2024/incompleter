# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/796008/cant-subtract-offset-naive-and-offset-aware-datetimes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.utils import timezone
    _l_(1540990)

except ImportError:
    pass
now_aware = _c_(1540993, _a_(1540992, _n_(1540991, "timezone", lambda: timezone), "now"))
_l_(1540994)

