# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
L = [_c_(1547535, _a_(1547530, _a_(1547529, _n_(1547528, "os", lambda: os), "path"), "join"), _c_(1547533, _a_(1547532, _n_(1547531, "os", lambda: os), "getcwd")),_n_(1547534, "f", lambda: f)) for f in _c_(1547538, _a_(1547537, _n_(1547536, "os", lambda: os), "listdir"), '.') if _c_(1547550, _a_(1547541, _a_(1547540, _n_(1547539, "os", lambda: os), "path"), "isfile"), _c_(1547549, _a_(1547544, _a_(1547543, _n_(1547542, "os", lambda: os), "path"), "join"), _c_(1547547, _a_(1547546, _n_(1547545, "os", lambda: os), "getcwd")),_n_(1547548, "f", lambda: f)))]
_l_(1547551)

