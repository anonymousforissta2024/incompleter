# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
somedict = {}
_l_(1540880)
_c_(1540883, _n_(1540881, "print", lambda: print), _n_(1540882, "somedict", lambda: somedict)[3]) # KeyError
_l_(1540884) # KeyError

someddict = _c_(1540887, _n_(1540885, "defaultdict", lambda: defaultdict), _n_(1540886, "int", lambda: int))
_l_(1540888)
_c_(1540891, _n_(1540889, "print", lambda: print), _n_(1540890, "someddict", lambda: someddict)[3]) # print int(), thus 0
_l_(1540892) # print int(), thus 0

