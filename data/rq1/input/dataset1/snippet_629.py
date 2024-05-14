# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1303243/how-to-find-out-if-a-python-object-is-a-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def isStr(o):
    _l_(1543527)

    aux = _c_(1543525, _n_(1543523, "repr", lambda: repr), _n_(1543524, "o", lambda: o))[-1] in '\'"'
    _l_(1543526)
    return aux

_c_(1543532, _a_(1543531, _c_(1543530, _n_(1543528, "repr", lambda: repr), _n_(1543529, "o", lambda: o))[-1:], "replace"), '"', "'") == "'"
_l_(1543533)

