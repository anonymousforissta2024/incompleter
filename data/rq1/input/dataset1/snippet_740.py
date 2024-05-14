# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use
# Python list with append()
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(1543633, _a_(1543629, _n_(1543628, "np", lambda: np), "mean"), _c_(1543632, _a_(1543631, _n_(1543630, "timeit", lambda: timeit), "repeat"), setup="a = []", stmt="a.append(1.0)", number=1000, repeat=5000)) * 1000
_l_(1543634)
# 0.054 +/- 0.025 msec

# Python array with append()
_c_(1543640, _a_(1543636, _n_(1543635, "np", lambda: np), "mean"), _c_(1543639, _a_(1543638, _n_(1543637, "timeit", lambda: timeit), "repeat"), setup="import array; a = array.array('f')", stmt="a.append(1.0)", number=1000, repeat=5000)) * 1000
_l_(1543641)
# 0.104 +/- 0.025 msec

# Numpy array with append()
_c_(1543647, _a_(1543643, _n_(1543642, "np", lambda: np), "mean"), _c_(1543646, _a_(1543645, _n_(1543644, "timeit", lambda: timeit), "repeat"), setup="import numpy as np; a = np.array([])", stmt="np.append(a, [1.0])", number=1000, repeat=5000)) * 1000
_l_(1543648)
# 5.183 +/- 0.950 msec

# Python list using +=
_c_(1543654, _a_(1543650, _n_(1543649, "np", lambda: np), "mean"), _c_(1543653, _a_(1543652, _n_(1543651, "timeit", lambda: timeit), "repeat"), setup="a = []", stmt="a += [1.0]", number=1000, repeat=5000)) * 1000
_l_(1543655)
# 0.062 +/- 0.021 msec

# Python array using += 
_c_(1543661, _a_(1543657, _n_(1543656, "np", lambda: np), "mean"), _c_(1543660, _a_(1543659, _n_(1543658, "timeit", lambda: timeit), "repeat"), setup="import array; a = array.array('f')", stmt="a += array.array('f', [1.0]) ", number=1000, repeat=5000)) * 1000
_l_(1543662)
# 0.289 +/- 0.043 msec

# Python list using extend()
_c_(1543668, _a_(1543664, _n_(1543663, "np", lambda: np), "mean"), _c_(1543667, _a_(1543666, _n_(1543665, "timeit", lambda: timeit), "repeat"), setup="a = []", stmt="a.extend([1.0])", number=1000, repeat=5000)) * 1000
_l_(1543669)
# 0.083 +/- 0.020 msec

# Python array using extend()
_c_(1543675, _a_(1543671, _n_(1543670, "np", lambda: np), "mean"), _c_(1543674, _a_(1543673, _n_(1543672, "timeit", lambda: timeit), "repeat"), setup="import array; a = array.array('f')", stmt="a.extend([1.0]) ", number=1000, repeat=5000)) * 1000
_l_(1543676)
# 0.169 +/- 0.034

