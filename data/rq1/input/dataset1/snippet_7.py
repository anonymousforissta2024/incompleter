# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/89228/how-do-i-execute-a-program-or-call-a-system-command
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import subprocess
    _l_(1547815)

except ImportError:
    pass
try:
    import sys
    _l_(1547817)

except ImportError:
    pass

# Some code here

pid = _c_(1547822, _a_(1547819, _n_(1547818, "subprocess", lambda: subprocess), "Popen"), [_a_(1547821, _n_(1547820, "sys", lambda: sys), "executable"), "longtask.py"]) # Call subprocess
_l_(1547823) # Call subprocess

# Some more code here

DETACHED_PROCESS = 0x00000008
_l_(1547824)

pid = _a_(1547831, _c_(1547830, _a_(1547826, _n_(1547825, "subprocess", lambda: subprocess), "Popen"), [_a_(1547828, _n_(1547827, "sys", lambda: sys), "executable"), "longtask.py"],
                       creationflags=_n_(1547829, "DETACHED_PROCESS", lambda: DETACHED_PROCESS)), "pid")
_l_(1547832)

pid = _c_(1547843, _a_(1547834, _n_(1547833, "subprocess", lambda: subprocess), "Popen"), [_a_(1547836, _n_(1547835, "sys", lambda: sys), "executable"), "longtask.py"], stdout=_a_(1547838, _n_(1547837, "subprocess", lambda: subprocess), "PIPE"), stderr=_a_(1547840, _n_(1547839, "subprocess", lambda: subprocess), "PIPE"), stdin=_a_(1547842, _n_(1547841, "subprocess", lambda: subprocess), "PIPE"))
_l_(1547844)

