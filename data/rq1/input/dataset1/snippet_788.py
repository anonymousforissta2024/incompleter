# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(1540996)

except ImportError:
    pass
try:
    import numpy as np
    _l_(1540998)

except ImportError:
    pass

class NumpyEncoder(_a_(1541000, _n_(1540999, "json", lambda: json), "JSONEncoder")):
    _l_(1541039)

    """ Special json encoder for numpy types """
    def default(self, obj):
        _l_(1541038)

        if _c_(1541005, _n_(1541001, "isinstance", lambda: isinstance), _n_(1541002, "obj", lambda: obj), _a_(1541004, _n_(1541003, "np", lambda: np), "integer")):
            _l_(1541030)

            aux = _c_(1541008, _n_(1541006, "int", lambda: int), _n_(1541007, "obj", lambda: obj))
            _l_(1541009)
            return aux
        elif _c_(1541014, _n_(1541010, "isinstance", lambda: isinstance), _n_(1541011, "obj", lambda: obj), _a_(1541013, _n_(1541012, "np", lambda: np), "floating")):
            _l_(1541029)

            aux = _c_(1541017, _n_(1541015, "float", lambda: float), _n_(1541016, "obj", lambda: obj))
            _l_(1541018)
            return aux
        elif _c_(1541023, _n_(1541019, "isinstance", lambda: isinstance), _n_(1541020, "obj", lambda: obj), _a_(1541022, _n_(1541021, "np", lambda: np), "ndarray")):
            _l_(1541028)

            aux = _c_(1541026, _a_(1541025, _n_(1541024, "obj", lambda: obj), "tolist"))
            _l_(1541027)
            return aux
        aux = _c_(1541036, _a_(1541033, _a_(1541032, _n_(1541031, "json", lambda: json), "JSONEncoder"), "default"), _n_(1541034, "self", lambda: self), _n_(1541035, "obj", lambda: obj))
        _l_(1541037)
        return aux

dumped = _c_(1541044, _a_(1541041, _n_(1541040, "json", lambda: json), "dumps"), _n_(1541042, "data", lambda: data), cls=_n_(1541043, "NumpyEncoder", lambda: NumpyEncoder))
_l_(1541045)

with _c_(1541048, _n_(1541046, "open", lambda: open), _n_(1541047, "path", lambda: path), 'w') as f:
    _l_(1541055)

    _c_(1541053, _a_(1541050, _n_(1541049, "json", lambda: json), "dump"), _n_(1541051, "dumped", lambda: dumped), _n_(1541052, "f", lambda: f))
    _l_(1541054)

