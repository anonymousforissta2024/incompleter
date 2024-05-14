# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6921699/can-i-get-json-to-load-into-an-ordereddict
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
my_ordered_dict = _c_(1547218, _a_(1547214, _n_(1547213, "json", lambda: json), "loads"), _n_(1547215, "json_str", lambda: json_str), object_pairs_hook=_a_(1547217, _n_(1547216, "collections", lambda: collections), "OrderedDict"))
_l_(1547219)
try:
    import simplejson as json
    _l_(1547221)

except ImportError:
    pass
try:
    import ordereddict
    _l_(1547223)

except ImportError:
    pass

my_ordered_dict = _c_(1547229, _a_(1547225, _n_(1547224, "json", lambda: json), "loads"), _n_(1547226, "json_str", lambda: json_str), object_pairs_hook=_a_(1547228, _n_(1547227, "ordereddict", lambda: ordereddict), "OrderedDict"))
_l_(1547230)

