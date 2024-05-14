# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(1543814)

except ImportError:
    pass
_c_(1543818, _a_(1543816, _n_(1543815, "re", lambda: re), "split"), '; |, ', _n_(1543817, "string_to_split", lambda: string_to_split))
_l_(1543819)

a='Beautiful, is; better*than\nugly'
_l_(1543820)
try:
    import re
    _l_(1543822)

except ImportError:
    pass
_c_(1543826, _a_(1543824, _n_(1543823, "re", lambda: re), "split"), '; |, |\*|\n',_n_(1543825, "a", lambda: a))
_l_(1543827)
['Beautiful', 'is', 'better', 'than', 'ugly']
_l_(1543828)

