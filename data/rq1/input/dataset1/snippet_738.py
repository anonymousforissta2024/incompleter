# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/436198/what-is-an-alternative-to-execfile-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def execfile(filepath, globals=None, locals=None):
    _l_(1538453)

    if _n_(1538430, "globals", lambda: globals) is None:
        _l_(1538432)

        globals = {}
        _l_(1538431)
    _c_(1538436, _a_(1538434, _n_(1538433, "globals", lambda: globals), "update"), {
        "__file__": _n_(1538435, "filepath", lambda: filepath),
        "__name__": "__main__",
    })
    _l_(1538437)
    with _c_(1538440, _n_(1538438, "open", lambda: open), _n_(1538439, "filepath", lambda: filepath), 'rb') as file:
        _l_(1538452)

        _c_(1538450, _n_(1538441, "exec", lambda: exec), _c_(1538447, _n_(1538442, "compile", lambda: compile), _c_(1538445, _a_(1538444, _n_(1538443, "file", lambda: file), "read")), _n_(1538446, "filepath", lambda: filepath), 'exec'), _n_(1538448, "globals", lambda: globals), _n_(1538449, "locals", lambda: locals))
        _l_(1538451)

# Execute the file.
_c_(1538455, _n_(1538454, "execfile", lambda: execfile), "/path/to/somefile.py")
_l_(1538456)

