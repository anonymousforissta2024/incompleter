# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
#!python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(1541297, _n_(1541296, "open", lambda: open), '/pythonwork/thefile_subset11.csv', 'w', newline='') as outfile:
    _l_(1541303)

    writer = _c_(1541301, _a_(1541299, _n_(1541298, "csv", lambda: csv), "writer"), _n_(1541300, "outfile", lambda: outfile))
    _l_(1541302)

#!python2
with _c_(1541305, _n_(1541304, "open", lambda: open), '/pythonwork/thefile_subset11.csv', 'wb') as outfile:
    _l_(1541311)

    writer = _c_(1541309, _a_(1541307, _n_(1541306, "csv", lambda: csv), "writer"), _n_(1541308, "outfile", lambda: outfile))
    _l_(1541310)

