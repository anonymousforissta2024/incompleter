# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
myfile = _c_(1545805, _n_(1545804, "open", lambda: open), "data.txt","r")
_l_(1545806)
data = ""
_l_(1545807)
lines = _c_(1545810, _a_(1545809, _n_(1545808, "myfile", lambda: myfile), "readlines"))
_l_(1545811)
for line in _n_(1545812, "lines", lambda: lines):
    _l_(1545818)

    data = _n_(1545813, "data", lambda: data) + _c_(1545816, _a_(1545815, _n_(1545814, "line", lambda: line), "strip"));
    _l_(1545817)

