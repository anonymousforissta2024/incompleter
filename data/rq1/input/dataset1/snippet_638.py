# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1158076/implement-touch-using-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1540343)

except ImportError:
    pass
def func(filename):
    _l_(1540360)

    if _c_(1540348, _a_(1540346, _a_(1540345, _n_(1540344, "os", lambda: os), "path"), "exists"), _n_(1540347, "filename", lambda: filename)):
        _l_(1540359)

        _c_(1540352, _a_(1540350, _n_(1540349, "os", lambda: os), "utime"), _n_(1540351, "filename", lambda: filename))
        _l_(1540353)
    else:
        with _c_(1540356, _n_(1540354, "open", lambda: open), _n_(1540355, "filename", lambda: filename),'a') as f:
            _l_(1540358)

            pass
            _l_(1540357)

_c_(1540366, _a_(1540362, _n_(1540361, "os", lambda: os), "utime"), _n_(1540363, "filename", lambda: filename),(_n_(1540364, "atime", lambda: atime),_n_(1540365, "mtime", lambda: mtime)))
_l_(1540367)

