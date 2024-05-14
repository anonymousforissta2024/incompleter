# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/306400/how-can-i-randomly-select-an-item-from-a-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
foo = ['a', 'b', 'c', 'd', 'e']
_l_(1548303)
number_of_samples = 1
_l_(1548304)

random_items = _c_(1548309, _a_(1548306, _n_(1548305, "random", lambda: random), "sample"), population=_n_(1548307, "foo", lambda: foo), k=_n_(1548308, "number_of_samples", lambda: number_of_samples))
_l_(1548310)

random_items = _c_(1548315, _a_(1548312, _n_(1548311, "random", lambda: random), "choices"), population=_n_(1548313, "foo", lambda: foo), k=_n_(1548314, "number_of_samples", lambda: number_of_samples))
_l_(1548316)

