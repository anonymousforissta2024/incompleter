# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime
    _l_(1547933)

except ImportError:
    pass
try:
    import pytz
    _l_(1547935)

except ImportError:
    pass

tz_NY = _c_(1547938, _a_(1547937, _n_(1547936, "pytz", lambda: pytz), "timezone"), 'America/New_York') 
_l_(1547939) 
datetime_NY = _c_(1547943, _a_(1547941, _n_(1547940, "datetime", lambda: datetime), "now"), _n_(1547942, "tz_NY", lambda: tz_NY))
_l_(1547944)
_c_(1547949, _n_(1547945, "print", lambda: print), "NY time:", _c_(1547948, _a_(1547947, _n_(1547946, "datetime_NY", lambda: datetime_NY), "strftime"), "%H:%M:%S"))
_l_(1547950)

tz_London = _c_(1547953, _a_(1547952, _n_(1547951, "pytz", lambda: pytz), "timezone"), 'Europe/London')
_l_(1547954)
datetime_London = _c_(1547958, _a_(1547956, _n_(1547955, "datetime", lambda: datetime), "now"), _n_(1547957, "tz_London", lambda: tz_London))
_l_(1547959)
_c_(1547964, _n_(1547960, "print", lambda: print), "London time:", _c_(1547963, _a_(1547962, _n_(1547961, "datetime_London", lambda: datetime_London), "strftime"), "%H:%M:%S"))
_l_(1547965)

tz_India = _c_(1547968, _a_(1547967, _n_(1547966, "pytz", lambda: pytz), "timezone"), 'Asia/India')
_l_(1547969)
datetime_India = _c_(1547973, _a_(1547971, _n_(1547970, "datetime", lambda: datetime), "now"), _n_(1547972, "tz_India", lambda: tz_India))
_l_(1547974)
_c_(1547979, _n_(1547975, "print", lambda: print), "India time:", _c_(1547978, _a_(1547977, _n_(1547976, "datetime_India", lambda: datetime_India), "strftime"), "%H:%M:%S"))
_l_(1547980)

#list timezones
_a_(1547982, _n_(1547981, "pytz", lambda: pytz), "all_timezones")
_l_(1547983)

