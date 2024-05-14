# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(1546482, _n_(1546481, "open", lambda: open), "foo.txt") as file:
    _l_(1546487)

    data = _c_(1546485, _a_(1546484, _n_(1546483, "file", lambda: file), "read"))
    _l_(1546486)

