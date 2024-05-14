# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/518021/is-arr-len-the-preferred-way-to-get-the-length-of-an-array-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import array
    _l_(1539264)

except ImportError:
    pass
arr = _c_(1539267, _a_(1539266, _n_(1539265, "array", lambda: array), "array"), 'i')
_l_(1539268)
_c_(1539271, _a_(1539270, _n_(1539269, "arr", lambda: arr), "append"), '2')
_l_(1539272)
_c_(1539275, _a_(1539274, _n_(1539273, "arr", lambda: arr), "__len__"))
_l_(1539276)
1
_l_(1539277)
_c_(1539280, _n_(1539278, "len", lambda: len), _n_(1539279, "arr", lambda: arr))
_l_(1539281)
1
_l_(1539282)

