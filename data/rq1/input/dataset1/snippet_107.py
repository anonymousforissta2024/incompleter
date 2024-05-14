# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(1548432)

except ImportError:
    pass
fig, ax = _c_(1548435, _a_(1548434, _n_(1548433, "plt", lambda: plt), "subplots"), nrows=1, ncols=1 )  # create figure & 1 axis
_l_(1548436)  # create figure & 1 axis
_c_(1548439, _a_(1548438, _n_(1548437, "ax", lambda: ax), "plot"), [0,1,2], [10,20,3])
_l_(1548440)
_c_(1548443, _a_(1548442, _n_(1548441, "fig", lambda: fig), "savefig"), 'path/to/save/image/to.png')   # save the figure to file
_l_(1548444)   # save the figure to file
_c_(1548448, _a_(1548446, _n_(1548445, "plt", lambda: plt), "close"), _n_(1548447, "fig", lambda: fig))    # close the figure window
_l_(1548449)    # close the figure window

