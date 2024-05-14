# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6591931/getting-file-size-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1547241)

except ImportError:
    pass
_c_(1547245, _a_(1547244, _a_(1547243, _n_(1547242, "os", lambda: os), "path"), "getsize"), 'C:\\Python27\\Lib\\genericpath.py')
_l_(1547246)
try:
    import os
    _l_(1547248)

except ImportError:
    pass
_a_(1547252, _c_(1547251, _a_(1547250, _n_(1547249, "os", lambda: os), "stat"), 'C:\\Python27\\Lib\\genericpath.py'), "st_size") 
_l_(1547253) 
try:
    from pathlib import Path
    _l_(1547255)

except ImportError:
    pass
_a_(1547260, _c_(1547259, _a_(1547258, _c_(1547257, _n_(1547256, "Path", lambda: Path), 'C:\\Python27\\Lib\\genericpath.py'), "stat")), "st_size")
_l_(1547261)

