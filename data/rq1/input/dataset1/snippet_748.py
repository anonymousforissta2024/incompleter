# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/26414913/normalize-columns-of-a-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df = _n_(1542127, "df", lambda: df)/_c_(1542134, _a_(1542131, _c_(1542130, _a_(1542129, _n_(1542128, "df", lambda: df), "max")), "astype"), _a_(1542133, _n_(1542132, "np", lambda: np), "float64"))
_l_(1542135)

df = _n_(1542136, "df", lambda: df)/_c_(1542147, _a_(1542144, _a_(1542138, _n_(1542137, "df", lambda: df), "loc")[_c_(1542143, _a_(1542142, _c_(1542141, _a_(1542140, _n_(1542139, "df", lambda: df), "abs")), "idxmax"))], "astype"), _a_(1542146, _n_(1542145, "np", lambda: np), "float64"))
_l_(1542148)

