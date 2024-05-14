# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8930915/append-a-dictionary-to-a-dictionary
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(1543419, _a_(1543417, _n_(1543416, "orig", lambda: orig), "update"), _n_(1543418, "extra", lambda: extra))    # Python 2.7+
_l_(1543420)    # Python 2.7+
orig |= _n_(1543421, "extra", lambda: extra)         # Python 3.9+
_l_(1543422)         # Python 3.9+

# Python 2.7+
dest = _c_(1543427, _a_(1543424, _n_(1543423, "collections", lambda: collections), "ChainMap"), _n_(1543425, "orig", lambda: orig), _n_(1543426, "extra", lambda: extra))
_l_(1543428)
dest = {_n_(1543429, "k", lambda: k): _n_(1543430, "v", lambda: v) for d in (_n_(1543431, "orig", lambda: orig), _n_(1543432, "extra", lambda: extra)) for (k, v) in _c_(1543435, _a_(1543434, _n_(1543433, "d", lambda: d), "items"))}
_l_(1543436)

# Python 3
dest = {**_n_(1543437, "orig", lambda: orig), **_n_(1543438, "extra", lambda: extra)}          
_l_(1543439)          
dest = {**_n_(1543440, "orig", lambda: orig), 'D': 4, 'E': 5}
_l_(1543441)

# Python 3.9+ 
dest = _n_(1543442, "orig", lambda: orig) | _n_(1543443, "extra", lambda: extra)
_l_(1543444)

orig  = {'A': 1, 'B': 2}
_l_(1543445)
extra = {'A': 3, 'C': 3}
_l_(1543446)

dest = _n_(1543447, "orig", lambda: orig) | _n_(1543448, "extra", lambda: extra)
_l_(1543449)
# dest = {'A': 3, 'B': 2, 'C': 3}

dest = _n_(1543450, "extra", lambda: extra) | _n_(1543451, "orig", lambda: orig)
_l_(1543452)
# dest = {'A': 1, 'B': 2, 'C': 3}

