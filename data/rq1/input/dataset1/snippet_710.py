# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7585307/how-to-correct-typeerror-unicode-objects-must-be-encoded-before-hashing
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import hashlib
    _l_(1539358)

except ImportError:
    pass
_c_(1539370, _a_(1539369, _c_(1539368, _a_(1539360, _n_(1539359, "hashlib", lambda: hashlib), "sha256"), _c_(1539367, _a_(1539366, _c_(1539365, _n_(1539361, "str", lambda: str), _c_(1539364, _a_(1539363, _n_(1539362, "random", lambda: random), "getrandbits"), 256)), "encode"), 'utf-8')), "hexdigest"))
_l_(1539371)
'cd183a211ed2434eac4f31b317c573c50e6c24e3a28b82ddcb0bf8bedf387a9f'
_l_(1539372)

