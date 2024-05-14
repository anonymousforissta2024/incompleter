# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/14770735/how-do-i-change-the-figure-size-with-subplots
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(1545999, _a_(1545998, _n_(1545997, "plt", lambda: plt), "figure"), figsize=(16, 8)) 
_l_(1546000) 
for i in _c_(1546002, _n_(1546001, "range", lambda: range), 1, 7):
    _l_(1546023)

    _c_(1546006, _a_(1546004, _n_(1546003, "plt", lambda: plt), "subplot"), 2, 3, _n_(1546005, "i", lambda: i))
    _l_(1546007)
    _c_(1546015, _a_(1546009, _n_(1546008, "plt", lambda: plt), "title"), _c_(1546014, _a_(1546010, 'Histogram of {}', "format"), _c_(1546013, _n_(1546011, "str", lambda: str), _n_(1546012, "i", lambda: i))))
    _l_(1546016)
    _c_(1546021, _a_(1546018, _n_(1546017, "plt", lambda: plt), "hist"), _n_(1546019, "x", lambda: x)[:,_n_(1546020, "i", lambda: i)-1], bins=60)
    _l_(1546022)

