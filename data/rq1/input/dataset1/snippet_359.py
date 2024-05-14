# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7065164/how-to-make-a-timezone-aware-datetime-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
unaware=_c_(1543016, _a_(1543015, _n_(1543014, "parser", lambda: parser), "parse"), "2020-05-01 0:00:00")
_l_(1543017)
aware=_c_(1543028, _a_(1543024, _c_(1543023, _a_(1543019, _n_(1543018, "unaware", lambda: unaware), "replace"), tzinfo=_c_(1543022, _a_(1543021, _n_(1543020, "tz", lambda: tz), "tzlocal"))), "astimezone"), _c_(1543027, _a_(1543026, _n_(1543025, "tz", lambda: tz), "tzlocal")))
_l_(1543029)

