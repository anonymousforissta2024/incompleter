# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8933237/how-do-i-check-if-directory-exists-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pathlib import Path
    _l_(1548870)

except ImportError:
    pass
_c_(1548874, _a_(1548873, _c_(1548872, _n_(1548871, "Path", lambda: Path), "/my/directory"), "mkdir"), parents=True, exist_ok=True)
_l_(1548875)
try:
    import os
    _l_(1548877)

except ImportError:
    pass
if not _c_(1548882, _a_(1548880, _a_(1548879, _n_(1548878, "os", lambda: os), "path"), "exists"), _n_(1548881, "directory", lambda: directory)):
    _l_(1548888)

    _c_(1548886, _a_(1548884, _n_(1548883, "os", lambda: os), "makedirs"), _n_(1548885, "directory", lambda: directory))
    _l_(1548887)
try:
    import os, errno
    _l_(1548890)

except ImportError:
    pass

try:
    _l_(1548904)

    _c_(1548894, _a_(1548892, _n_(1548891, "os", lambda: os), "makedirs"), _n_(1548893, "directory", lambda: directory))
    _l_(1548895)
except _n_(1548896, "OSError", lambda: OSError) as e:
    _l_(1548903)

    if _a_(1548898, _n_(1548897, "e", lambda: e), "errno") != _a_(1548900, _n_(1548899, "errno", lambda: errno), "EEXIST"):
        _l_(1548902)

        raise
        _l_(1548901)

try:
    _l_(1548912)

    _c_(1548907, _a_(1548906, _n_(1548905, "os", lambda: os), "makedirs"), "path/to/directory")
    _l_(1548908)
except _n_(1548909, "FileExistsError", lambda: FileExistsError):
    _l_(1548911)

    # directory already exists
    pass
    _l_(1548910)

_c_(1548915, _a_(1548914, _n_(1548913, "os", lambda: os), "makedirs"), "path/to/directory", exist_ok=True)  # succeeds even if directory exists.
_l_(1548916)  # succeeds even if directory exists.

