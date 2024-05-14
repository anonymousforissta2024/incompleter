# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
count_row = _a_(121733, _n_(121732, "df", lambda: df), "shape")[0]  # Gives number of rows
_l_(121734)  # Gives number of rows
count_col = _a_(121736, _n_(121735, "df", lambda: df), "shape")[1]  # Gives number of columns
_l_(121737)  # Gives number of columns

r, c = _a_(121739, _n_(121738, "df", lambda: df), "shape")
_l_(121740)

