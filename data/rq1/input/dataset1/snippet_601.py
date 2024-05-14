# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1373164/how-do-i-create-variable-variables
# using dictionary
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
variables = {}
_l_(1538403)
_n_(1538404, "variables", lambda: variables)["first"] = 34
_l_(1538405)
_n_(1538406, "variables", lambda: variables)["second"] = 45
_l_(1538407)
_c_(1538411, _n_(1538408, "print", lambda: print), _n_(1538409, "variables", lambda: variables)["first"], _n_(1538410, "variables", lambda: variables)["second"])
_l_(1538412)

# using namedtuple
Variables = _c_(1538414, _n_(1538413, "namedtuple", lambda: namedtuple), 'Variables', ['first', 'second'])
_l_(1538415)
vars = _c_(1538417, _n_(1538416, "Variables", lambda: Variables), 34, 45)
_l_(1538418)
_c_(1538424, _n_(1538419, "print", lambda: print), _a_(1538421, _n_(1538420, "vars", lambda: vars), "first"), _a_(1538423, _n_(1538422, "vars", lambda: vars), "second"))
_l_(1538425)

