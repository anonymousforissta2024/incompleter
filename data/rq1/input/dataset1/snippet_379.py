# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1543217)

except ImportError:
    pass
try:
    import glob
    _l_(1543219)

except ImportError:
    pass
try:
    import pandas
    _l_(1543221)

except ImportError:
    pass
try:
    from collections import OrderedDict
    _l_(1543223)

except ImportError:
    pass
path =r'C:\DRO\DCL_rawdata_files'
_l_(1543224)
filenames = _c_(1543228, _a_(1543226, _n_(1543225, "glob", lambda: glob), "glob"), _n_(1543227, "path", lambda: path) + "/*.csv")
_l_(1543229)

dict_of_df = _c_(1543237, _n_(1543230, "OrderedDict", lambda: OrderedDict), ((_n_(1543231, "f", lambda: f), _c_(1543235, _a_(1543233, _n_(1543232, "pandas", lambda: pandas), "read_csv"), _n_(1543234, "f", lambda: f))) for f in _n_(1543236, "filenames", lambda: filenames)))
_l_(1543238)
_c_(1543242, _a_(1543240, _n_(1543239, "pandas", lambda: pandas), "concat"), _n_(1543241, "dict_of_df", lambda: dict_of_df), sort=True)
_l_(1543243)

