# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import io
    _l_(1540288)

except ImportError:
    pass
try:
    import requests
    _l_(1540290)

except ImportError:
    pass

r = _c_(1540293, _a_(1540292, _n_(1540291, "requests", lambda: requests), "get"), 'http://lorempixel.com/400/200')
_l_(1540294)
_c_(1540297, _a_(1540296, _n_(1540295, "r", lambda: r), "raise_for_status"))
_l_(1540298)
with _c_(1540303, _a_(1540300, _n_(1540299, "io", lambda: io), "BytesIO"), _a_(1540302, _n_(1540301, "r", lambda: r), "content")) as f:
    _l_(1540313)

    with _c_(1540307, _a_(1540305, _n_(1540304, "Image", lambda: Image), "open"), _n_(1540306, "f", lambda: f)) as img:
        _l_(1540312)

        _c_(1540310, _a_(1540309, _n_(1540308, "img", lambda: img), "show"))
        _l_(1540311)
try:
    import requests
    _l_(1540315)

except ImportError:
    pass

r = _c_(1540318, _a_(1540317, _n_(1540316, "requests", lambda: requests), "get"), 'http://lorempixel.com/400/200', stream=True)
_l_(1540319)
_c_(1540322, _a_(1540321, _n_(1540320, "r", lambda: r), "raise_for_status"))
_l_(1540323)
_a_(1540325, _n_(1540324, "r", lambda: r), "raw").decode_content = True  # Required to decompress gzip/deflate compressed responses.
_l_(1540326)  # Required to decompress gzip/deflate compressed responses.
with _c_(1540332, _a_(1540329, _a_(1540328, _n_(1540327, "PIL", lambda: PIL), "Image"), "open"), _a_(1540331, _n_(1540330, "r", lambda: r), "raw")) as img:
    _l_(1540337)

    _c_(1540335, _a_(1540334, _n_(1540333, "img", lambda: img), "show"))
    _l_(1540336)
_c_(1540340, _a_(1540339, _n_(1540338, "r", lambda: r), "close"))  # Safety when stream=True ensure the connection is released.
_l_(1540341)  # Safety when stream=True ensure the connection is released.

