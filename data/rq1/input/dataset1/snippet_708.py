# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9786102/how-do-i-parallelize-a-simple-python-loop
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tqdm.contrib.concurrent import thread_map, process_map
    _l_(1542816)

except ImportError:
    pass


def calc_stuff(num, multiplier):
    _l_(1542827)

    try:
        import time
        _l_(1542818)

    except ImportError:
        pass

    _c_(1542821, _a_(1542820, _n_(1542819, "time", lambda: time), "sleep"), 1)
    _l_(1542822)
    aux = _n_(1542823, "num", lambda: num), _n_(1542824, "num", lambda: num) * _n_(1542825, "multiplier", lambda: multiplier)
    _l_(1542826)

    return aux


if _n_(1542828, "__name__", lambda: __name__) == "__main__":
    _l_(1542848)


    # let's parallelize this for loop:
    # results = [calc_stuff(i, 2) for i in range(64)]

    loop_idx = _c_(1542830, _n_(1542829, "range", lambda: range), 64)
    _l_(1542831)
    multiplier = [2] * _c_(1542834, _n_(1542832, "len", lambda: len), _n_(1542833, "loop_idx", lambda: loop_idx))
    _l_(1542835)

    # either with threading:
    results_threading = _c_(1542840, _n_(1542836, "thread_map", lambda: thread_map), _n_(1542837, "calc_stuff", lambda: calc_stuff), _n_(1542838, "loop_idx", lambda: loop_idx), _n_(1542839, "multiplier", lambda: multiplier))
    _l_(1542841)

    # or with multi-processing:
    results_processes = _c_(1542846, _n_(1542842, "process_map", lambda: process_map), _n_(1542843, "calc_stuff", lambda: calc_stuff), _n_(1542844, "loop_idx", lambda: loop_idx), _n_(1542845, "multiplier", lambda: multiplier))
    _l_(1542847)

