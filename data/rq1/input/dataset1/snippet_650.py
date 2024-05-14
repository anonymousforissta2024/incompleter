# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5658369/how-to-input-a-regex-in-string-replace
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(1543727)

except ImportError:
    pass
line = _c_(1543731, _a_(1543729, _n_(1543728, "re", lambda: re), "sub"), r"</?\[\d+>", "", _n_(1543730, "line", lambda: line))
_l_(1543732)

line = _c_(1543736, _a_(1543734, _n_(1543733, "re", lambda: re), "sub"), r"""
  (?x) # Use free-spacing mode.
  <    # Match a literal '<'
  /?   # Optionally match a '/'
  \[   # Match a literal '['
  \d+  # Match one or more digits
  >    # Match a literal '>'
  """, "", _n_(1543735, "line", lambda: line))
_l_(1543737)

