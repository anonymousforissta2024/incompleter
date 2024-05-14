# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import socket
    _l_(1541763)

except ImportError:
    pass
def getNetworkIp():
    _l_(1541788)

    s = _c_(1541770, _a_(1541765, _n_(1541764, "socket", lambda: socket), "socket"), _a_(1541767, _n_(1541766, "socket", lambda: socket), "AF_INET"), _a_(1541769, _n_(1541768, "socket", lambda: socket), "SOCK_DGRAM"))
    _l_(1541771)
    _c_(1541778, _a_(1541773, _n_(1541772, "s", lambda: s), "setsockopt"), _a_(1541775, _n_(1541774, "socket", lambda: socket), "SOL_SOCKET"), _a_(1541777, _n_(1541776, "socket", lambda: socket), "SO_BROADCAST"), 1)
    _l_(1541779)
    _c_(1541782, _a_(1541781, _n_(1541780, "s", lambda: s), "connect"), ('<broadcast>', 0))
    _l_(1541783)
    aux = _c_(1541786, _a_(1541785, _n_(1541784, "s", lambda: s), "getsockname"))[0]
    _l_(1541787)
    return aux

_c_(1541792, _n_(1541789, "print", lambda: print), _c_(1541791, _n_(1541790, "getNetworkIp", lambda: getNetworkIp)))
_l_(1541793)

