# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/180986/what-is-the-difference-between-re-search-and-re-match
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(1538353, _a_(1538352, _n_(1538351, "re", lambda: re), "search"), 'test', ' test')      # returns a Truthy match object (because the search starts from any index) 
_l_(1538354)      # returns a Truthy match object (because the search starts from any index) 

_c_(1538357, _a_(1538356, _n_(1538355, "re", lambda: re), "match"), 'test', ' test')       # returns None (because the search start from 0 index)
_l_(1538358)       # returns None (because the search start from 0 index)
_c_(1538361, _a_(1538360, _n_(1538359, "re", lambda: re), "match"), 'test', 'test')        # returns a Truthy match object (match at 0 index)
_l_(1538362)        # returns a Truthy match object (match at 0 index)

