# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/735975/static-methods-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(1548686, _a_(1548685, _n_(1548684, "ClassName", lambda: ClassName), "StaticMethod"))
_l_(1548687)

class ClassName(_n_(1548688, "object", lambda: object)):
    _l_(1548692)


    @_n_(1548689, "staticmethod", lambda: staticmethod)
    def static_method(kwarg1=None):
        _l_(1548691)

        '''return a value that is a function of kwarg1'''
        _l_(1548690)

class ClassName(_n_(1548693, "object", lambda: object)):
    _l_(1548699)


    def static_method(kwarg1=None):
        _l_(1548695)

        '''return a value that is a function of kwarg1'''
        _l_(1548694)

    static_method = _c_(1548697, _n_(1548696, "staticmethod", lambda: staticmethod), static_method)
    _l_(1548698)

_c_(1548702, _a_(1548701, _n_(1548700, "ClassName", lambda: ClassName), "static_method"))
_l_(1548703)

class ClassName(_n_(1548704, "object", lambda: object)):
    _l_(1548708)


    @_n_(1548705, "classmethod", lambda: classmethod)
    def class_method(cls, kwarg1=None):
        _l_(1548707)

        '''return a value that is a function of the class and kwarg1'''
        _l_(1548706)

new_instance = _c_(1548711, _a_(1548710, _n_(1548709, "ClassName", lambda: ClassName), "class_method"))
_l_(1548712)

new_dict = _c_(1548715, _a_(1548714, _n_(1548713, "dict", lambda: dict), "fromkeys"), ['key1', 'key2'])
_l_(1548716)

