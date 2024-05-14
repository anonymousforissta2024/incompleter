# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2827623/how-can-i-create-an-object-and-add-attributes-to-it
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(1547364, "obj", lambda: obj).a = _c_(1547367, _n_(1547365, "type", lambda: type), 'Test', (_n_(1547366, "object", lambda: object),), {})  
_l_(1547368)  
_a_(1547370, _n_(1547369, "obj", lambda: obj), "a").b = 'fun'  
_l_(1547371)  

_n_(1547372, "obj", lambda: obj).b = lambda:None
_l_(1547373)

class Test:
  _l_(1547375)

  pass
  _l_(1547374)
_n_(1547376, "obj", lambda: obj).c = _c_(1547378, _n_(1547377, "Test", lambda: Test))
_l_(1547379)

