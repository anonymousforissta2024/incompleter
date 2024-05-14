# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/209840/how-can-i-make-a-dictionary-dict-from-separate-lists-of-keys-and-values
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
dict = {_n_(1548667, "item", lambda: item) : _n_(1548668, "values", lambda: values)[_n_(1548669, "index", lambda: index)] for index, item in _c_(1548672, _n_(1548670, "enumerate", lambda: enumerate), _n_(1548671, "keys", lambda: keys))}
_l_(1548673)

dict = {}
_l_(1548674)
for index, item in _c_(1548677, _n_(1548675, "enumerate", lambda: enumerate), _n_(1548676, "keys", lambda: keys)):
    _l_(1548683)

    _n_(1548678, "dict", lambda: dict)[_n_(1548679, "item", lambda: item)] = _n_(1548680, "values", lambda: values)[_n_(1548681, "index", lambda: index)]
    _l_(1548682)

