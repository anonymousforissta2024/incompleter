# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import hashlib
    _l_(1541908)

except ImportError:
    pass
with _c_(1541910, _n_(1541909, "open", lambda: open), "your_filename.txt", "rb") as f:
    _l_(1541924)

    file_hash = _c_(1541913, _a_(1541912, _n_(1541911, "hashlib", lambda: hashlib), "md5"))
    _l_(1541914)
    while chunk := _c_(1541917, _a_(1541916, _n_(1541915, "f", lambda: f), "read"), 8192):
        _l_(1541923)

        _c_(1541921, _a_(1541919, _n_(1541918, "file_hash", lambda: file_hash), "update"), _n_(1541920, "chunk", lambda: chunk))
        _l_(1541922)

_c_(1541929, _n_(1541925, "print", lambda: print), _c_(1541928, _a_(1541927, _n_(1541926, "file_hash", lambda: file_hash), "digest")))
_l_(1541930)
_c_(1541935, _n_(1541931, "print", lambda: print), _c_(1541934, _a_(1541933, _n_(1541932, "file_hash", lambda: file_hash), "hexdigest")))  # to get a printable str instead of bytes
_l_(1541936)  # to get a printable str instead of bytes

