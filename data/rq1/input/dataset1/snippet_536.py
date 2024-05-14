# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/546321/how-do-i-calculate-the-date-six-months-from-the-current-date-using-the-datetime
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import timedelta
    _l_(1540070)

except ImportError:
    pass
try:
    from dateutil.relativedelta import relativedelta
    _l_(1540072)

except ImportError:
    pass

end_date = _n_(1540073, "start_date", lambda: start_date) + _c_(1540076, _n_(1540074, "relativedelta", lambda: relativedelta), months=_n_(1540075, "delta_period", lambda: delta_period)) + _c_(1540079, _n_(1540077, "timedelta", lambda: timedelta), days=-_n_(1540078, "delta_period", lambda: delta_period))
_l_(1540080)

