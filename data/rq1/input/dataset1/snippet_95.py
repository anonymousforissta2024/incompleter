# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MyException(_n_(1549000, "Exception", lambda: Exception)):
    _l_(1549002)

    pass
    _l_(1549001)

raise _c_(1549004, _n_(1549003, "MyException", lambda: MyException), "My hovercraft is full of eels")
_l_(1549005)

raise _c_(1549007, _n_(1549006, "MyException", lambda: MyException), {"message":"My hovercraft is full of animals", "animal":"eels"})
_l_(1549008)

try:
    _l_(1549021)

    raise _c_(1549010, _n_(1549009, "MyException", lambda: MyException), {"message":"My hovercraft is full of animals", "animal":"eels"})
    _l_(1549011)
except _n_(1549012, "MyException", lambda: MyException) as e:
    _l_(1549020)

    details = _a_(1549014, _n_(1549013, "e", lambda: e), "args")[0]
    _l_(1549015)
    _c_(1549018, _n_(1549016, "print", lambda: print), _n_(1549017, "details", lambda: details)["animal"])
    _l_(1549019)

class MyError(_n_(1549022, "Exception", lambda: Exception)):
    _l_(1549034)

    def __init__(self, message, animal):
        _l_(1549029)

        _n_(1549023, "self", lambda: self).message = _n_(1549024, "message", lambda: message)
        _l_(1549025)
        _n_(1549026, "self", lambda: self).animal = _n_(1549027, "animal", lambda: animal)
        _l_(1549028)
    def __str__(self):
        _l_(1549033)

        aux = _a_(1549031, _n_(1549030, "self", lambda: self), "message")
        _l_(1549032)
        return aux

