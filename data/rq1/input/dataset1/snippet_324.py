# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6618002/using-property-versus-getters-and-setters
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Account(_n_(1542149, "object", lambda: object)):
    _l_(1542165)

    @_n_(1542150, "property", lambda: property)
    def email(self):
        _l_(1542154)

        aux = _a_(1542152, _n_(1542151, "self", lambda: self), "_email")
        _l_(1542153)
        return aux

    @_a_(1542155, email, "setter")
    def email(self, value):
        _l_(1542164)

        if '@' not in _n_(1542156, "value", lambda: value):
            _l_(1542160)

            raise _c_(1542158, _n_(1542157, "ValueError", lambda: ValueError), 'Invalid email address.')
            _l_(1542159)
        _n_(1542161, "self", lambda: self)._email = _n_(1542162, "value", lambda: value)
        _l_(1542163)

a = _c_(1542167, _n_(1542166, "Account", lambda: Account))
_l_(1542168)
_n_(1542169, "a", lambda: a).email = 'badaddress'
_l_(1542170)

class Account(_n_(1542171, "object", lambda: object)):
    _l_(1542180)

    ...
    _l_(1542172)
    def validate(self):
        _l_(1542179)

        if '@' not in _a_(1542174, _n_(1542173, "self", lambda: self), "email"):
            _l_(1542178)

            raise _c_(1542176, _n_(1542175, "ValueError", lambda: ValueError), 'Invalid email address.')
            _l_(1542177)

