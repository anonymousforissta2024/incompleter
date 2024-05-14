# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/646644/how-to-get-last-items-of-a-list-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(1542347, "num_list", lambda: num_list)[-9:]
_l_(1542348)

_n_(1542349, "sequence", lambda: sequence)[_n_(1542350, "start", lambda: start):_n_(1542351, "stop", lambda: stop):_n_(1542352, "step", lambda: step)]
_l_(1542353)

list_copy = _n_(1542354, "sequence", lambda: sequence)[:]
_l_(1542355)

del my_list[:]
_l_(1542356)

last_nine_slice = _c_(1542358, _n_(1542357, "slice", lambda: slice), -9, None)
_l_(1542359)

_c_(1542363, _n_(1542360, "list", lambda: list), _c_(1542362, _n_(1542361, "range", lambda: range), 100))[_n_(1542364, "last_nine_slice", lambda: last_nine_slice)]
_l_(1542365)
[91, 92, 93, 94, 95, 96, 97, 98, 99]
_l_(1542366)
try:
    from itertools import islice
    _l_(1542368)

except ImportError:
    pass
_c_(1542374, _n_(1542369, "islice", lambda: islice), _c_(1542373, _n_(1542370, "reversed", lambda: reversed), _c_(1542372, _n_(1542371, "range", lambda: range), 100)), 0, 9)
_l_(1542375)

_c_(1542383, _n_(1542376, "list", lambda: list), _c_(1542382, _n_(1542377, "islice", lambda: islice), _c_(1542381, _n_(1542378, "reversed", lambda: reversed), _c_(1542380, _n_(1542379, "range", lambda: range), 100)), 0, 9))
_l_(1542384)
[99, 98, 97, 96, 95, 94, 93, 92, 91]
_l_(1542385)

