# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4697882/how-can-i-find-all-matches-to-a-regular-expression-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(1546033, _a_(1546032, _n_(1546031, "re", lambda: re), "findall"), r'all (.*?) are', 'all cats are smarter than dogs, all dogs are dumber than cats')
_l_(1546034)
# Output: ['cats', 'dogs']

[_c_(1546037, _a_(1546036, _n_(1546035, "x", lambda: x), "group")) for x in _c_(1546040, _a_(1546039, _n_(1546038, "re", lambda: re), "finditer"), r'all (.*?) are', 'all cats are smarter than dogs, all dogs are dumber than cats')]
_l_(1546041)
# Output: ['all cats are', 'all dogs are']

