# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/744373/what-happens-when-using-mutual-or-circular-cyclic-imports
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from b import B
    _l_(1540369)

except ImportError:
    pass

class A:
    _l_(1540392)

    @_n_(1540370, "staticmethod", lambda: staticmethod)
    def save_result(result):
        _l_(1540374)

        _c_(1540372, _n_(1540371, "print", lambda: print), 'save the result')
        _l_(1540373)

    @_n_(1540375, "staticmethod", lambda: staticmethod)
    def do_something_a_ish(param):
        _l_(1540384)

        _c_(1540382, _a_(1540377, _n_(1540376, "A", lambda: A), "save_result"), _c_(1540381, _a_(1540379, _n_(1540378, "A", lambda: A), "use_param_like_a_would"), _n_(1540380, "param", lambda: param)))
        _l_(1540383)
    
    @_n_(1540385, "staticmethod", lambda: staticmethod)
    def do_something_related_to_b(param):
        _l_(1540391)

        _c_(1540389, _a_(1540387, _n_(1540386, "B", lambda: B), "do_something_b_ish"), _n_(1540388, "param", lambda: param))
        _l_(1540390)
try:
    from a import A
    _l_(1540394)

except ImportError:
    pass

class B:
    _l_(1540405)

    @_n_(1540395, "staticmethod", lambda: staticmethod)
    def do_something_b_ish(param):
        _l_(1540404)

        _c_(1540402, _a_(1540397, _n_(1540396, "A", lambda: A), "save_result"), _c_(1540401, _a_(1540399, _n_(1540398, "B", lambda: B), "use_param_like_b_would"), _n_(1540400, "param", lambda: param)))
        _l_(1540403)

def save_result(result):
    _l_(1540409)

    _c_(1540407, _n_(1540406, "print", lambda: print), 'save the result')
    _l_(1540408)
try:
    from b import B
    _l_(1540411)

except ImportError:
    pass
try:
    from c import save_result
    _l_(1540413)

except ImportError:
    pass

class A:
    _l_(1540430)

    @_n_(1540414, "staticmethod", lambda: staticmethod)
    def do_something_a_ish(param):
        _l_(1540422)

        _c_(1540420, _n_(1540415, "save_result", lambda: save_result), _c_(1540419, _a_(1540417, _n_(1540416, "A", lambda: A), "use_param_like_a_would"), _n_(1540418, "param", lambda: param)))
        _l_(1540421)
    
    @_n_(1540423, "staticmethod", lambda: staticmethod)
    def do_something_related_to_b(param):
        _l_(1540429)

        _c_(1540427, _a_(1540425, _n_(1540424, "B", lambda: B), "do_something_b_ish"), _n_(1540426, "param", lambda: param))
        _l_(1540428)
try:
    from c import save_result
    _l_(1540432)

except ImportError:
    pass

class B:
    _l_(1540442)

    @_n_(1540433, "staticmethod", lambda: staticmethod)
    def do_something_b_ish(param):
        _l_(1540441)

        _c_(1540439, _n_(1540434, "save_result", lambda: save_result), _c_(1540438, _a_(1540436, _n_(1540435, "B", lambda: B), "use_param_like_b_would"), _n_(1540437, "param", lambda: param)))
        _l_(1540440)

