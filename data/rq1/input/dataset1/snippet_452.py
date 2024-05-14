# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1118183/how-to-debug-in-django-the-good-way
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_a_(1544691, _n_(1544690, "register", lambda: register), "filter") 
def pdb(element):
    _l_(1544699)

    try:
        import pdb; 
        _l_(1544696)

    except ImportError:
        pass
    aux = _n_(1544697, "element", lambda: element)
    _l_(1544698)
    return aux

