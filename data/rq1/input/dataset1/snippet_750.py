# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(1543771)

except ImportError:
    pass

url = 'https://www.python.org/static/img/python-logo.png'
_l_(1543772)
fileName = 'D:\Python\dwnldPythonLogo.png'
_l_(1543773)
req = _c_(1543777, _a_(1543775, _n_(1543774, "requests", lambda: requests), "get"), _n_(1543776, "url", lambda: url))
_l_(1543778)
file = _c_(1543781, _n_(1543779, "open", lambda: open), _n_(1543780, "fileName", lambda: fileName), 'wb')
_l_(1543782)
for chunk in _c_(1543785, _a_(1543784, _n_(1543783, "req", lambda: req), "iter_content"), 100000):
    _l_(1543791)

    _c_(1543789, _a_(1543787, _n_(1543786, "file", lambda: file), "write"), _n_(1543788, "chunk", lambda: chunk))
    _l_(1543790)
_c_(1543794, _a_(1543793, _n_(1543792, "file", lambda: file), "close"))
_l_(1543795)

