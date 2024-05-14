# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1305532/how-to-convert-a-nested-python-dict-to-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class obj(_n_(1543088, "object", lambda: object)):
    _l_(1543127)

    def __init__(self, d):
        _l_(1543126)

        for k, v in _c_(1543091, _a_(1543090, _n_(1543089, "d", lambda: d), "items")):
            _l_(1543125)

            if _c_(1543096, _n_(1543092, "isinstance", lambda: isinstance), _n_(1543093, "k", lambda: k), (_n_(1543094, "list", lambda: list), _n_(1543095, "tuple", lambda: tuple))):
                _l_(1543124)

                _c_(1543109, _n_(1543097, "setattr", lambda: setattr), _n_(1543098, "self", lambda: self), _n_(1543099, "k", lambda: k), [_c_(1543102, _n_(1543100, "obj", lambda: obj), _n_(1543101, "x", lambda: x)) if _c_(1543106, _n_(1543103, "isinstance", lambda: isinstance), _n_(1543104, "x", lambda: x), _n_(1543105, "dict", lambda: dict)) else _n_(1543107, "x", lambda: x) for x in _n_(1543108, "v", lambda: v)])
                _l_(1543110)
            else:
                _c_(1543122, _n_(1543111, "setattr", lambda: setattr), _n_(1543112, "self", lambda: self), _n_(1543113, "k", lambda: k), _c_(1543116, _n_(1543114, "obj", lambda: obj), _n_(1543115, "v", lambda: v)) if _c_(1543120, _n_(1543117, "isinstance", lambda: isinstance), _n_(1543118, "v", lambda: v), _n_(1543119, "dict", lambda: dict)) else _n_(1543121, "v", lambda: v))
                _l_(1543123)

d = {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar"}]}
_l_(1543128)
x = _c_(1543131, _n_(1543129, "obj", lambda: obj), _n_(1543130, "d", lambda: d))
_l_(1543132)
_a_(1543135, _a_(1543134, _n_(1543133, "x", lambda: x), "b"), "c")
_l_(1543136)
2
_l_(1543137)
_a_(1543140, _a_(1543139, _n_(1543138, "x", lambda: x), "d")[1], "foo")
_l_(1543141)
'bar'
_l_(1543142)

