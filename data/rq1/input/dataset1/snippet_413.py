# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
min_value = _c_(1544631, _n_(1544629, "min", lambda: min), _n_(1544630, "values", lambda: values))
_l_(1544632)
indexes_with_min_value = [_n_(1544633, "i", lambda: i) for i in _c_(1544638, _n_(1544634, "range", lambda: range), 0,_c_(1544637, _n_(1544635, "len", lambda: len), _n_(1544636, "values", lambda: values))) if _n_(1544639, "values", lambda: values)[_n_(1544640, "i", lambda: i)] == _n_(1544641, "min_value", lambda: min_value)]
_l_(1544642)

choosen = _n_(1544643, "indexes_with_min_value", lambda: indexes_with_min_value)[0]
_l_(1544644)

