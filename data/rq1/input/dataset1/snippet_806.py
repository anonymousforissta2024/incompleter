# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2225564/get-a-filtered-list-of-files-in-a-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
files = [_n_(1539990, "f", lambda: f) for f in _c_(1539993, _a_(1539992, _n_(1539991, "os", lambda: os), "listdir"), '.') if _c_(1539997, _a_(1539995, _n_(1539994, "re", lambda: re), "match"), r'[0-9]+.*\.jpg', _n_(1539996, "f", lambda: f))]
_l_(1539998)

