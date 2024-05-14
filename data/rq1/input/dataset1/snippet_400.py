# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13331698/how-to-apply-a-function-to-two-columns-of-pandas-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(1542212)

except ImportError:
    pass

df = _c_(1542215, _a_(1542214, _n_(1542213, "pd", lambda: pd), "DataFrame"), {'ID':['1','2','3'], 'col_1': [0,2,3], 'col_2':[1,4,5]})
_l_(1542216)
mylist = ['a','b','c','d','e','f']
_l_(1542217)

def get_sublist(sta,end):
    _l_(1542222)

    aux = _n_(1542218, "mylist", lambda: mylist)[_n_(1542219, "sta", lambda: sta):_n_(1542220, "end", lambda: end)+1]
    _l_(1542221)
    return aux

def get_sublist_list(cols):
    _l_(1542228)

    aux = [_c_(1542226, _n_(1542223, "get_sublist", lambda: get_sublist), _n_(1542224, "cols", lambda: cols)[0],_n_(1542225, "cols", lambda: cols)[1])]
    _l_(1542227)
    return aux

def unlist(list_of_lists):
    _l_(1542231)

    aux = _n_(1542229, "list_of_lists", lambda: list_of_lists)[0]
    _l_(1542230)
    return aux

_n_(1542232, "df", lambda: df)['col_3'] = _c_(1542239, _a_(1542237, _c_(1542236, _a_(1542234, _n_(1542233, "df", lambda: df)[['col_1','col_2']], "apply"), _n_(1542235, "get_sublist_list", lambda: get_sublist_list),axis=1), "apply"), _n_(1542238, "unlist", lambda: unlist))
_l_(1542240)

_n_(1542241, "df", lambda: df)
_l_(1542242)

