# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4186062/sqlalchemy-order-by-descending
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
session = _c_(1541210, _n_(1541209, "Session", lambda: Session))
_l_(1541211)
auth_client_name = 'client3' 
_l_(1541212) 
result_by_auth_client = _c_(1541229, _a_(1541228, _c_(1541227, _a_(1541222, _c_(1541221, _a_(1541217, _c_(1541216, _a_(1541214, _n_(1541213, "session", lambda: session), "query"), _n_(1541215, "ClientTotal", lambda: ClientTotal)), "filter"), _a_(1541219, _n_(1541218, "ClientTotal", lambda: ClientTotal), "client") ==
_n_(1541220, "auth_client_name", lambda: auth_client_name)), "order_by"), _c_(1541226, _a_(1541225, _a_(1541224, _n_(1541223, "ClientTotal", lambda: ClientTotal), "id"), "desc"))), "all"))
_l_(1541230)

for rbac in _n_(1541231, "result_by_auth_client", lambda: result_by_auth_client):
    _l_(1541237)

    _c_(1541235, _n_(1541232, "print", lambda: print), _a_(1541234, _n_(1541233, "rbac", lambda: rbac), "id")) 
    _l_(1541236) 
_c_(1541240, _a_(1541239, _n_(1541238, "session", lambda: session), "close"))
_l_(1541241)

