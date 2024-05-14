# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/332289/how-do-i-change-the-size-of-figures-drawn-with-matplotlib
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
fig = _c_(1548004, _a_(1548003, _a_(1548002, _n_(1548001, "matplotlib", lambda: matplotlib), "pyplot"), "gcf"))
_l_(1548005)
_c_(1548008, _a_(1548007, _n_(1548006, "fig", lambda: fig), "set_size_inches"), 18.5, 10.5)
_l_(1548009)
_c_(1548012, _a_(1548011, _n_(1548010, "fig", lambda: fig), "savefig"), 'test2png.png', dpi=100)
_l_(1548013)

_c_(1548016, _a_(1548015, _n_(1548014, "fig", lambda: fig), "set_size_inches"), 18.5, 10.5, forward=True)
_l_(1548017)

_c_(1548020, _a_(1548019, _n_(1548018, "fig", lambda: fig), "set_dpi"), 100)
_l_(1548021)

