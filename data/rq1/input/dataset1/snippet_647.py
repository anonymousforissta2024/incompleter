# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20199126/reading-json-from-a-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(1539583)

except ImportError:
    pass
df = _c_(1539586, _a_(1539585, _n_(1539584, "pd", lambda: pd), "read_json"), 'strings.json', lines=True)
_l_(1539587)
_c_(1539590, _n_(1539588, "print", lambda: print), _n_(1539589, "df", lambda: df))
_l_(1539591)

