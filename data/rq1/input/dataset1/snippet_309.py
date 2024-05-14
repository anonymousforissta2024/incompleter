# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/772124/what-does-the-ellipsis-object-do
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Foo:
    _l_(1546465)

    bar: Any = ...
    _l_(1546462)
    def __init__(self, name: _n_(1546463, "str", lambda: str)=...) -> None:
        _l_(1546464)

...
