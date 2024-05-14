# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/33054527/typeerror-a-bytes-like-object-is-required-not-str-when-writing-to-a-file-in
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for line in _n_(1542181, "lines", lambda: lines):
    _l_(1542193)

    _c_(1542186, _n_(1542182, "print", lambda: print), _c_(1542185, _n_(1542183, "type", lambda: type), _n_(1542184, "line", lambda: line)))# <class 'bytes'>
    _l_(1542187)# <class 'bytes'>
    if 'substring' in _n_(1542188, "line", lambda: line):
        _l_(1542192)

        _c_(1542190, _n_(1542189, "print", lambda: print), 'success')
        _l_(1542191)

for line in _n_(1542194, "lines", lambda: lines):
    _l_(1542210)

    line = _c_(1542197, _a_(1542196, _n_(1542195, "line", lambda: line), "decode"))
    _l_(1542198)
    _c_(1542203, _n_(1542199, "print", lambda: print), _c_(1542202, _n_(1542200, "type", lambda: type), _n_(1542201, "line", lambda: line)))# <class 'str'>
    _l_(1542204)# <class 'str'>
    if 'substring' in _n_(1542205, "line", lambda: line):
        _l_(1542209)

        _c_(1542207, _n_(1542206, "print", lambda: print), 'success')
        _l_(1542208)

