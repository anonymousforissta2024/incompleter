# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2128505/difference-between-filter-and-filter-by-in-sqlalchemy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def filter_by(self, **kwargs):
    _l_(1546171)

    aux = _c_(1546169, _a_(1546164, _n_(1546163, "self", lambda: self), "filter"), _c_(1546168, _a_(1546166, _n_(1546165, "sql", lambda: sql), "and_"), **_n_(1546167, "kwargs", lambda: kwargs)))
    _l_(1546170)
    return aux

_c_(1546178, _a_(1546177, _c_(1546176, _a_(1546173, _n_(1546172, "session", lambda: session), "query"), _a_(1546175, _n_(1546174, "db", lambda: db), "users")), "filter_by"), name='Joe', surname='Dodson')
_l_(1546179)

_c_(1546194, _a_(1546185, _c_(1546184, _a_(1546181, _n_(1546180, "session", lambda: session), "query"), _a_(1546183, _n_(1546182, "db", lambda: db), "users")), "filter"), _c_(1546193, _n_(1546186, "or_", lambda: or_), _a_(1546189, _a_(1546188, _n_(1546187, "db", lambda: db), "users"), "name")=='Ryan', _a_(1546192, _a_(1546191, _n_(1546190, "db", lambda: db), "users"), "country")=='England'))
_l_(1546195)

_c_(1546208, _a_(1546201, _c_(1546200, _a_(1546197, _n_(1546196, "session", lambda: session), "query"), _a_(1546199, _n_(1546198, "db", lambda: db), "users")), "filter"), (_a_(1546204, _a_(1546203, _n_(1546202, "db", lambda: db), "users"), "name")=='Ryan') | (_a_(1546207, _a_(1546206, _n_(1546205, "db", lambda: db), "users"), "country")=='England'))
_l_(1546209)

_c_(1546213, _a_(1546212, _a_(1546211, _n_(1546210, "Users", lambda: Users), "query"), "get"), 123)
_l_(1546214)
# And even by a composite PK
_c_(1546218, _a_(1546217, _a_(1546216, _n_(1546215, "Users", lambda: Users), "query"), "get"), 123, 321)
_l_(1546219)

