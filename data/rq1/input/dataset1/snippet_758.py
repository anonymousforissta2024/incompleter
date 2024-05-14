# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6444548/how-do-i-get-the-picture-size-with-pil
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(1538878)

except ImportError:
    pass

im = _c_(1538881, _a_(1538880, _n_(1538879, "Image", lambda: Image), "open"), 'whatever.png')
_l_(1538882)
width, height = _a_(1538884, _n_(1538883, "im", lambda: im), "size")
_l_(1538885)

