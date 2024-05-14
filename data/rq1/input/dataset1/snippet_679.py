# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/31594549/how-to-change-the-figure-size-of-a-seaborn-axes-or-figure-level-plot
# Sets the figure size temporarily but has to be set again the next plot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(1539425, _a_(1539424, _n_(1539423, "plt", lambda: plt), "figure"), figsize=(18,18))
_l_(1539426)

_c_(1539433, _a_(1539428, _n_(1539427, "sns", lambda: sns), "barplot"), x=_a_(1539430, _n_(1539429, "housing", lambda: housing), "ocean_proximity"), y=_a_(1539432, _n_(1539431, "housing", lambda: housing), "median_house_value"))
_l_(1539434)
_c_(1539437, _a_(1539436, _n_(1539435, "plt", lambda: plt), "show"))
_l_(1539438)

