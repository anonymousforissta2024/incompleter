# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5574702/how-do-i-print-to-stderr-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(1548598, "print", lambda: print) >> _a_(1548600, _n_(1548599, "sys", lambda: sys), "stderr"), 'spam' 
_l_(1548601) 

_c_(1548605, _n_(1548602, "print", lambda: print), "spam", file=_a_(1548604, _n_(1548603, "sys", lambda: sys), "stderr")) 
_l_(1548606) 

