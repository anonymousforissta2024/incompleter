# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/276052/how-to-get-current-cpu-and-ram-usage-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1541504)

except ImportError:
    pass
try:
    import re
    _l_(1541506)

except ImportError:
    pass

CUT_OFF = 90
_l_(1541507)

def get_cpu_load():
    _l_(1541541)

    cmd = "ps -Ao user,uid,comm,pid,pcpu --sort=-pcpu | head -n 2 | tail -1"
    _l_(1541508)
    response = _c_(1541514, _a_(1541513, _c_(1541512, _a_(1541510, _n_(1541509, "os", lambda: os), "popen"), _n_(1541511, "cmd", lambda: cmd), 'r'), "read"))
    _l_(1541515)
    arr = _c_(1541519, _a_(1541517, _n_(1541516, "re", lambda: re), "findall"), r'\S+', _n_(1541518, "response", lambda: response))
    _l_(1541520)
    _c_(1541523, _n_(1541521, "print", lambda: print), _n_(1541522, "arr", lambda: arr))
    _l_(1541524)
    needKill = _c_(1541527, _n_(1541525, "float", lambda: float), _n_(1541526, "arr", lambda: arr)[-1]) > _n_(1541528, "CUT_OFF", lambda: CUT_OFF)
    _l_(1541529)
    if _n_(1541530, "needKill", lambda: needKill):
        _l_(1541540)

        r = _c_(1541534, _a_(1541532, _n_(1541531, "os", lambda: os), "popen"), f"kill -9 {_n_(1541533, 'arr', lambda: arr)[-2]}")
        _l_(1541535)
        _c_(1541538, _n_(1541536, "print", lambda: print), 'kill:', _n_(1541537, "r", lambda: r))
        _l_(1541539)

if _n_(1541542, "__name__", lambda: __name__) == '__main__':
    _l_(1541548)

    # Test CPU with 
    # $ stress --cpu 1
    # crontab -e
    # Every 1 min
    # */1 * * * * sh dog.sh
    # ctlr o, ctlr x
    # crontab -l
    _c_(1541546, _n_(1541543, "print", lambda: print), _c_(1541545, _n_(1541544, "get_cpu_load", lambda: get_cpu_load)))
    _l_(1541547)

