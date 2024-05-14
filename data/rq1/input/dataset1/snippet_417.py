# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/44778/how-would-you-make-a-comma-separated-string-from-a-list-of-strings
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(1542925)

except ImportError:
    pass
with _c_(1542927, _n_(1542926, "open", lambda: open), 'some.csv', 'w', newline='') as f:
    _l_(1542938)

    writer = _c_(1542931, _a_(1542929, _n_(1542928, "csv", lambda: csv), "writer"), _n_(1542930, "f", lambda: f))
    _l_(1542932)
    _c_(1542936, _a_(1542934, _n_(1542933, "writer", lambda: writer), "writerow"), _n_(1542935, "l", lambda: l))  # this will output l as a single row.  
    _l_(1542937)  # this will output l as a single row.  

