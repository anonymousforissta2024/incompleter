# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
s_str: _n_(1548860, "str", lambda: str) = "\x00\x01\x00\xc0\x01\x00\x00\x00\x04"
_l_(1548861)

s_bytes: _n_(1548862, "bytes", lambda: bytes) = b'\x00\x01\x00\xc0\x01\x00\x00\x00\x04'
_l_(1548863)

s_new: _n_(1548864, "bytes", lambda: bytes) = _c_(1548867, _n_(1548865, "bytes", lambda: bytes), _n_(1548866, "s", lambda: s), encoding="raw_unicode_escape")
_l_(1548868)

