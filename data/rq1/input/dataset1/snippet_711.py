# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8220801/how-to-use-timeit-module
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import timeit
    _l_(1546272)

except ImportError:
    pass

start_time = _c_(1546275, _a_(1546274, _n_(1546273, "timeit", lambda: timeit), "default_timer"))
_l_(1546276)
_c_(1546278, _n_(1546277, "func1", lambda: func1))
_l_(1546279)
_c_(1546285, _n_(1546280, "print", lambda: print), _c_(1546283, _a_(1546282, _n_(1546281, "timeit", lambda: timeit), "default_timer")) - _n_(1546284, "start_time", lambda: start_time))
_l_(1546286)

start_time = _c_(1546289, _a_(1546288, _n_(1546287, "timeit", lambda: timeit), "default_timer"))
_l_(1546290)
_c_(1546292, _n_(1546291, "func2", lambda: func2))
_l_(1546293)
_c_(1546299, _n_(1546294, "print", lambda: print), _c_(1546297, _a_(1546296, _n_(1546295, "timeit", lambda: timeit), "default_timer")) - _n_(1546298, "start_time", lambda: start_time))
_l_(1546300)

