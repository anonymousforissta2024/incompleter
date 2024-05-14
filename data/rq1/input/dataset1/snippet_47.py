# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11346283/renaming-column-names-in-pandas
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
new_cols = ['a', 'b', 'c', 'd', 'e']
_l_(1547845)
new_names_map = {_a_(1547847, _n_(1547846, "df", lambda: df), "columns")[_n_(1547848, "i", lambda: i)]:_n_(1547849, "new_cols", lambda: new_cols)[_n_(1547850, "i", lambda: i)] for i in _c_(1547855, _n_(1547851, "range", lambda: range), _c_(1547854, _n_(1547852, "len", lambda: len), _n_(1547853, "new_cols", lambda: new_cols)))}
_l_(1547856)

_c_(1547860, _a_(1547858, _n_(1547857, "df", lambda: df), "rename"), _n_(1547859, "new_names_map", lambda: new_names_map), axis=1, inplace=True)
_l_(1547861)

