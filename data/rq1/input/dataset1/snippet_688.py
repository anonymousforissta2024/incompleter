# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/19125722/adding-a-legend-to-pyplot-in-matplotlib-in-the-simplest-manner-possible
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
first = [1, 2, 4, 5, 4]
_l_(1543319)
second = [3, 4, 2, 2, 3]
_l_(1543320)
_c_(1543325, _a_(1543322, _n_(1543321, "plt", lambda: plt), "plot"), _n_(1543323, "first", lambda: first), 'g--', _n_(1543324, "second", lambda: second), 'r--')
_l_(1543326)
_c_(1543329, _a_(1543328, _n_(1543327, "plt", lambda: plt), "legend"), ['First List', 'Second List'], loc='upper left')
_l_(1543330)
_c_(1543333, _a_(1543332, _n_(1543331, "plt", lambda: plt), "show"))
_l_(1543334)

