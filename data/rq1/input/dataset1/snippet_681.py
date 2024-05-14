# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2077897/substitute-multiple-whitespace-with-single-whitespace-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(1539544)

except ImportError:
    pass

_RE_COMBINE_WHITESPACE = _c_(1539547, _a_(1539546, _n_(1539545, "re", lambda: re), "compile"), r"\s+")
_l_(1539548)

my_str = _c_(1539554, _a_(1539553, _c_(1539552, _a_(1539550, _n_(1539549, "_RE_COMBINE_WHITESPACE", lambda: _RE_COMBINE_WHITESPACE), "sub"), " ", _n_(1539551, "my_str", lambda: my_str)), "strip"))
_l_(1539555)
try:
    import re
    _l_(1539557)

except ImportError:
    pass

_RE_COMBINE_WHITESPACE = _c_(1539560, _a_(1539559, _n_(1539558, "re", lambda: re), "compile"), r"(?a:\s+)")
_l_(1539561)
_RE_STRIP_WHITESPACE = _c_(1539564, _a_(1539563, _n_(1539562, "re", lambda: re), "compile"), r"(?a:^\s+|\s+$)")
_l_(1539565)

my_str = _c_(1539569, _a_(1539567, _n_(1539566, "_RE_COMBINE_WHITESPACE", lambda: _RE_COMBINE_WHITESPACE), "sub"), " ", _n_(1539568, "my_str", lambda: my_str))
_l_(1539570)
my_str = _c_(1539574, _a_(1539572, _n_(1539571, "_RE_STRIP_WHITESPACE", lambda: _RE_STRIP_WHITESPACE), "sub"), "", _n_(1539573, "my_str", lambda: my_str))
_l_(1539575)

