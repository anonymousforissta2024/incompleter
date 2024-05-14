# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4284313/how-can-i-check-the-syntax-of-python-script-without-executing-it
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(1545254)

except ImportError:
    pass
try:
    import glob, os
    _l_(1545256)

except ImportError:
    pass

_c_(1545261, _a_(1545258, _n_(1545257, "os", lambda: os), "chdir"), _a_(1545260, _n_(1545259, "sys", lambda: sys), "argv")[1])
_l_(1545262)
for file in _c_(1545265, _a_(1545264, _n_(1545263, "glob", lambda: glob), "glob"), "*.py"):
    _l_(1545277)

    source = _c_(1545270, _a_(1545269, _c_(1545268, _n_(1545266, "open", lambda: open), _n_(1545267, "file", lambda: file), 'r'), "read")) + '\n'
    _l_(1545271)
    _c_(1545275, _n_(1545272, "compile", lambda: compile), _n_(1545273, "source", lambda: source), _n_(1545274, "file", lambda: file), 'exec')
    _l_(1545276)

