# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/32370281/how-to-embed-image-or-picture-in-jupyter-notebook-either-from-a-local-machine-o
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(1538541)

except ImportError:
    pass
try:
    from ipywidgets import Image
    _l_(1538543)

except ImportError:
    pass

_c_(1538549, _n_(1538544, "Image", lambda: Image), value=_a_(1538548, _c_(1538547, _a_(1538546, _n_(1538545, "requests", lambda: requests), "get"), 'https://octodex.github.com/images/yaktocat.png'), "content"))
_l_(1538550)

