# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/17043860/how-to-dump-a-dict-to-a-json-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
d = {"name":"interpolator",
     "children":[{'name':_n_(1539346, "key", lambda: key),"size":_n_(1539347, "value", lambda: value)} for key,value in _c_(1539350, _a_(1539349, _n_(1539348, "sample", lambda: sample), "items"))]}
_l_(1539351)
json_string = _c_(1539355, _a_(1539353, _n_(1539352, "json", lambda: json), "dumps"), _n_(1539354, "d", lambda: d))
_l_(1539356)

