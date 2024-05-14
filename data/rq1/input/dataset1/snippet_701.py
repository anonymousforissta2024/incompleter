# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5055042/whats-the-best-practice-using-a-settings-file-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import yaml
    _l_(1541092)

except ImportError:
    pass
config = _c_(1541097, _a_(1541094, _n_(1541093, "yaml", lambda: yaml), "safe_load"), _c_(1541096, _n_(1541095, "open", lambda: open), "path/to/config.yml"))
_l_(1541098)

