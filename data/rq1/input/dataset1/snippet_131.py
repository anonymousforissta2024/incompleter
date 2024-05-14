# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
## Standalone boilerplate before relative imports
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _n_(1548041, "__package__", lambda: __package__) is None:
    _l_(1548061)

    DIR = _a_(1548047, _c_(1548046, _a_(1548045, _c_(1548044, _n_(1548042, "Path", lambda: Path), _n_(1548043, "__file__", lambda: __file__)), "resolve")), "parent")
    _l_(1548048)
    _c_(1548056, _a_(1548051, _a_(1548050, _n_(1548049, "sys", lambda: sys), "path"), "insert"), 0, _c_(1548055, _n_(1548052, "str", lambda: str), _a_(1548054, _n_(1548053, "DIR", lambda: DIR), "parent")))
    _l_(1548057)
    __package__ = _a_(1548059, _n_(1548058, "DIR", lambda: DIR), "name")
    _l_(1548060)
try:
    from . import variable_in__init__py
    _l_(1548063)

except ImportError:
    pass
try:
    from . import other_module_in_package
    _l_(1548065)

except ImportError:
    pass

