# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/21494489/what-does-numpy-random-seed0-do
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(1540649, _a_(1540648, _a_(1540647, _n_(1540646, "np", lambda: np), "random"), "seed"), 2)
_l_(1540650)
_c_(1540654, _a_(1540653, _a_(1540652, _n_(1540651, "np", lambda: np), "random"), "randn"), 2) # array([-0.41675785, -0.05626683])
_l_(1540655) # array([-0.41675785, -0.05626683])
_c_(1540659, _a_(1540658, _a_(1540657, _n_(1540656, "np", lambda: np), "random"), "randn"), 1) # array([-1.24528809])
_l_(1540660) # array([-1.24528809])

_c_(1540664, _a_(1540663, _a_(1540662, _n_(1540661, "np", lambda: np), "random"), "seed"), 2)
_l_(1540665)
_c_(1540669, _a_(1540668, _a_(1540667, _n_(1540666, "np", lambda: np), "random"), "randn"), 1) # array([-0.41675785])
_l_(1540670) # array([-0.41675785])
_c_(1540674, _a_(1540673, _a_(1540672, _n_(1540671, "np", lambda: np), "random"), "randn"), 2) # array([-0.05626683, -1.24528809])
_l_(1540675) # array([-0.05626683, -1.24528809])

