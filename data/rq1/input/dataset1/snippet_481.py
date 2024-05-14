# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10840533/most-pythonic-way-to-delete-a-file-which-may-not-exist
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    _l_(1540007)

    _c_(1540002, _a_(1540000, _n_(1539999, "os", lambda: os), "remove"), _n_(1540001, "filename", lambda: filename))
    _l_(1540003)
except _n_(1540004, "FileNotFoundError", lambda: FileNotFoundError):
    _l_(1540006)

    pass
    _l_(1540005)

