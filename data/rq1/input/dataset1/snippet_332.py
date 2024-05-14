# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29576430/shuffle-dataframe-rows
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(1542434, _a_(1542431, _a_(1542430, _n_(1542429, "np", lambda: np), "random"), "shuffle"), _a_(1542433, _n_(1542432, "DataFrame", lambda: DataFrame), "values"))
_l_(1542435)

nd = _c_(1542440, _a_(1542438, _a_(1542437, _n_(1542436, "sklearn", lambda: sklearn), "utils"), "shuffle"), _n_(1542439, "nd", lambda: nd))
_l_(1542441)

_c_(1542446, _a_(1542444, _a_(1542443, _n_(1542442, "np", lambda: np), "random"), "shuffle"), _n_(1542445, "nd", lambda: nd))
_l_(1542447)

df = _c_(1542452, _a_(1542450, _a_(1542449, _n_(1542448, "sklearn", lambda: sklearn), "utils"), "shuffle"), _n_(1542451, "df", lambda: df))
_l_(1542453)

_c_(1542459, _a_(1542456, _a_(1542455, _n_(1542454, "np", lambda: np), "random"), "shuffle"), _a_(1542458, _n_(1542457, "df", lambda: df), "values"))
_l_(1542460)
try:
    import timeit
    _l_(1542462)

except ImportError:
    pass
setup = '''
import numpy as np
import pandas as pd
import sklearn
nd = np.random.random((1000, 100))
df = pd.DataFrame(nd)
'''
_l_(1542463)

_c_(1542467, _a_(1542465, _n_(1542464, "timeit", lambda: timeit), "timeit"), 'nd = sklearn.utils.shuffle(nd)', setup=_n_(1542466, "setup", lambda: setup), number=1000)
_l_(1542468)
_c_(1542472, _a_(1542470, _n_(1542469, "timeit", lambda: timeit), "timeit"), 'np.random.shuffle(nd)', setup=_n_(1542471, "setup", lambda: setup), number=1000)
_l_(1542473)
_c_(1542477, _a_(1542475, _n_(1542474, "timeit", lambda: timeit), "timeit"), 'df = sklearn.utils.shuffle(df)', setup=_n_(1542476, "setup", lambda: setup), number=1000)
_l_(1542478)
_c_(1542482, _a_(1542480, _n_(1542479, "timeit", lambda: timeit), "timeit"), 'np.random.shuffle(df.values)', setup=_n_(1542481, "setup", lambda: setup), number=1000)
_l_(1542483)

