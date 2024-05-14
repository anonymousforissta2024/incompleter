# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3013449/list-comprehension-vs-lambda-filter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
[_n_(1541370, "x", lambda: x) for x in _n_(1541371, "X", lambda: X) if _c_(1541374, _n_(1541372, "P", lambda: P), _n_(1541373, "x", lambda: x))]
_l_(1541375)

[_c_(1541378, _n_(1541376, "f", lambda: f), _n_(1541377, "x", lambda: x)) for x in _n_(1541379, "X", lambda: X) if _c_(1541384, _n_(1541380, "P", lambda: P), _c_(1541383, _n_(1541381, "f", lambda: f), _n_(1541382, "x", lambda: x)))]
_l_(1541385)

primes_cubed = [_n_(1541386, "x", lambda: x)*_n_(1541387, "x", lambda: x)*_n_(1541388, "x", lambda: x) for x in _c_(1541390, _n_(1541389, "range", lambda: range), 1000) if _c_(1541393, _n_(1541391, "prime", lambda: prime), _n_(1541392, "x", lambda: x))]
_l_(1541394)

prime_cubes = [_n_(1541395, "x", lambda: x)*_n_(1541396, "x", lambda: x)*_n_(1541397, "x", lambda: x) for x in _c_(1541399, _n_(1541398, "range", lambda: range), 1000) if _c_(1541404, _n_(1541400, "prime", lambda: prime), _n_(1541401, "x", lambda: x)*_n_(1541402, "x", lambda: x)*_n_(1541403, "x", lambda: x))]
_l_(1541405)

prime_cubes = _c_(1541413, _n_(1541406, "filter", lambda: filter), _n_(1541407, "prime", lambda: prime), [_n_(1541408, "x", lambda: x)*_n_(1541409, "x", lambda: x)*_n_(1541410, "x", lambda: x) for x in _c_(1541412, _n_(1541411, "range", lambda: range), 1000)])
_l_(1541414)

