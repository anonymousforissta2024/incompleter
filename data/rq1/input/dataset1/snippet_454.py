# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/107705/disable-output-buffering
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(1541628)

except ImportError:
    pass
myFile= _c_(1541630, _n_(1541629, "open", lambda: open), "a.log", "w", 0 ) 
_l_(1541631) 
_n_(1541632, "sys", lambda: sys).stdout= _n_(1541633, "myFile", lambda: myFile)
_l_(1541634)

