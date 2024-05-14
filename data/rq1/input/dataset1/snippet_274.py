# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6392739/what-does-the-at-symbol-do-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df = _c_(1544504, _a_(1544503, _n_(1544502, "pandas", lambda: pandas), "DataFrame"), {'foo': [1,2,15,17]})
_l_(1544505)
y = 10
_l_(1544506)
_n_(1544507, "df", lambda: df) >> _c_(1544509, _n_(1544508, "query", lambda: query), 'foo > @y') # plydata
_l_(1544510) # plydata
_c_(1544513, _a_(1544512, _n_(1544511, "df", lambda: df), "query"), 'foo > @y') # pandas
_l_(1544514) # pandas

