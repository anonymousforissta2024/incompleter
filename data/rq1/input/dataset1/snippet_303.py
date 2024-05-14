# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/15112125/how-to-test-multiple-variables-for-equality-against-a-single-value
# ✅ test multiple variables against single value using tuple

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if 'a' in (_n_(1547306, "a", lambda: a), _n_(1547307, "b", lambda: b), _n_(1547308, "c", lambda: c)):
    _l_(1547312)

    _c_(1547310, _n_(1547309, "print", lambda: print), 'value is stored in at least one of the variables')
    _l_(1547311)

# ---------------------------------------------------------

# ✅ test multiple variables against single value using tuple

if 'a' in {_n_(1547313, "a", lambda: a), _n_(1547314, "b", lambda: b), _n_(1547315, "c", lambda: c)}:
    _l_(1547319)

    _c_(1547317, _n_(1547316, "print", lambda: print), 'value is stored in at least one of the variables')
    _l_(1547318)

# ---------------------------------------------------------


# ✅ test multiple variables against single value (OR operator chaining)
if _n_(1547320, "a", lambda: a) == 'a' or _n_(1547321, "b", lambda: b) == 'a' or _n_(1547322, "c", lambda: c) == 'a':
    _l_(1547326)

    _c_(1547324, _n_(1547323, "print", lambda: print), 'value is stored in at least one of the variables')
    _l_(1547325)

