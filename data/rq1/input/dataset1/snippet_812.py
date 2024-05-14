# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/15411107/delete-a-dictionary-item-if-the-key-exists
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
keys_to_remove = _c_(1540115, _a_(1540109, _c_(1540108, _n_(1540106, "set", lambda: set), _n_(1540107, "keys", lambda: keys)), "intersection"), _c_(1540114, _n_(1540110, "set", lambda: set), _c_(1540113, _a_(1540112, _n_(1540111, "mydict", lambda: mydict), "keys"))))
_l_(1540116)
for key in _n_(1540117, "keys_to_remove", lambda: keys_to_remove):
    _l_(1540119)

    del mydict[key]
    _l_(1540118)

keys_to_keep = _c_(1540124, _n_(1540120, "set", lambda: set), _c_(1540123, _a_(1540122, _n_(1540121, "mydict", lambda: mydict), "keys"))) - _c_(1540127, _n_(1540125, "set", lambda: set), _n_(1540126, "keys", lambda: keys))
_l_(1540128)
new_dict = {_n_(1540129, "k", lambda: k): _n_(1540130, "v", lambda: v) for k, v in _c_(1540133, _a_(1540132, _n_(1540131, "mydict", lambda: mydict), "iteritems")) if _n_(1540134, "k", lambda: k) in _n_(1540135, "keys_to_keep", lambda: keys_to_keep)}
_l_(1540136)

keys_to_keep = _c_(1540141, _n_(1540137, "set", lambda: set), _c_(1540140, _a_(1540139, _n_(1540138, "mydict", lambda: mydict), "keys"))) - _c_(1540144, _n_(1540142, "set", lambda: set), _n_(1540143, "keys", lambda: keys))
_l_(1540145)
new_dict = {_n_(1540146, "k", lambda: k): _n_(1540147, "mydict", lambda: mydict)[_n_(1540148, "k", lambda: k)] for k in _n_(1540149, "keys_to_keep", lambda: keys_to_keep)}
_l_(1540150)

