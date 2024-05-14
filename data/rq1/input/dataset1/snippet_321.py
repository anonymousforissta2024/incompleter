# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5626193/what-is-monkey-patching
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(1539467)

except ImportError:
    pass
def just_foo_cols(self):
    _l_(1539473)

    """Get a list of column names containing the string 'foo'

    """
    aux = [_n_(1539468, "x", lambda: x) for x in _a_(1539470, _n_(1539469, "self", lambda: self), "columns") if 'foo' in _n_(1539471, "x", lambda: x)]
    _l_(1539472)
    return aux

_a_(1539475, _n_(1539474, "pd", lambda: pd), "DataFrame").just_foo_cols = _n_(1539476, "just_foo_cols", lambda: just_foo_cols) # monkey-patch the DataFrame class
_l_(1539477) # monkey-patch the DataFrame class
df = _c_(1539484, _a_(1539479, _n_(1539478, "pd", lambda: pd), "DataFrame"), [_c_(1539483, _n_(1539480, "list", lambda: list), _c_(1539482, _n_(1539481, "range", lambda: range), 4))], columns=["A","foo","foozball","bar"])
_l_(1539485)
_c_(1539488, _a_(1539487, _n_(1539486, "df", lambda: df), "just_foo_cols"))
_l_(1539489)
del pd.DataFrame.just_foo_cols # you can also remove the new method
_l_(1539490) # you can also remove the new method
try:
    import pandas as pd
    _l_(1539492)

except ImportError:
    pass

def just_foo_cols(self):
    _l_(1539498)

    """Get a list of column names containing the string 'foo'

    """
    aux = [_n_(1539493, "x", lambda: x) for x in _a_(1539495, _n_(1539494, "self", lambda: self), "columns") if 'foo' in _n_(1539496, "x", lambda: x)]
    _l_(1539497)
    return aux

_a_(1539500, _n_(1539499, "pd", lambda: pd), "DataFrame").just_foo_cols = _n_(1539501, "just_foo_cols", lambda: just_foo_cols) # monkey-patch the DataFrame class
_l_(1539502) # monkey-patch the DataFrame class

df = _c_(1539509, _a_(1539504, _n_(1539503, "pd", lambda: pd), "DataFrame"), [_c_(1539508, _n_(1539505, "list", lambda: list), _c_(1539507, _n_(1539506, "range", lambda: range), 4))], columns=["A","foo","foozball","bar"])
_l_(1539510)
_c_(1539513, _a_(1539512, _n_(1539511, "df", lambda: df), "just_foo_cols"))
_l_(1539514)
del pd.DataFrame.just_foo_cols # you can also remove the new method
_l_(1539515) # you can also remove the new method
try:
    import datasource
    _l_(1539517)

except ImportError:
    pass

def get_data(self):
    _l_(1539522)

    '''monkey patch datasource.Structure with this to simulate error'''
    _l_(1539518)
    raise _a_(1539520, _n_(1539519, "datasource", lambda: datasource), "DataRetrievalError")
    _l_(1539521)

_a_(1539524, _n_(1539523, "datasource", lambda: datasource), "Structure").get_data = _n_(1539525, "get_data", lambda: get_data)
_l_(1539526)

def setUp(self):
    _l_(1539536)

    # retain a pointer to the actual real method:
    _n_(1539527, "self", lambda: self).real_get_data = _a_(1539530, _a_(1539529, _n_(1539528, "datasource", lambda: datasource), "Structure"), "get_data")
    _l_(1539531)
    # monkey patch it:
    _a_(1539533, _n_(1539532, "datasource", lambda: datasource), "Structure").get_data = _n_(1539534, "get_data", lambda: get_data)
    _l_(1539535)

def tearDown(self):
    _l_(1539542)

    # give the real method back to the Structure object:
    _a_(1539538, _n_(1539537, "datasource", lambda: datasource), "Structure").get_data = _a_(1539540, _n_(1539539, "self", lambda: self), "real_get_data")
    _l_(1539541)

