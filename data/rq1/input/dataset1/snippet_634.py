# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/36013063/what-is-the-purpose-of-meshgrid-in-python-numpy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sinus2d(x, y):
    _l_(1544780)

    aux = _c_(1544774, _a_(1544772, _n_(1544771, "np", lambda: np), "sin"), _n_(1544773, "x", lambda: x)) + _c_(1544778, _a_(1544776, _n_(1544775, "np", lambda: np), "sin"), _n_(1544777, "y", lambda: y))
    _l_(1544779)
    return aux

xx, yy = _c_(1544793, _a_(1544782, _n_(1544781, "np", lambda: np), "meshgrid"), _c_(1544787, _a_(1544784, _n_(1544783, "np", lambda: np), "linspace"), 0,2*_a_(1544786, _n_(1544785, "np", lambda: np), "pi"),100), _c_(1544792, _a_(1544789, _n_(1544788, "np", lambda: np), "linspace"), 0,2*_a_(1544791, _n_(1544790, "np", lambda: np), "pi"),100))
_l_(1544794)
z = _c_(1544798, _n_(1544795, "sinus2d", lambda: sinus2d), _n_(1544796, "xx", lambda: xx), _n_(1544797, "yy", lambda: yy)) # Create the image on this grid
_l_(1544799) # Create the image on this grid
try:
    import matplotlib.pyplot as plt
    _l_(1544801)

except ImportError:
    pass
_c_(1544805, _a_(1544803, _n_(1544802, "plt", lambda: plt), "imshow"), _n_(1544804, "z", lambda: z), origin='lower', interpolation='none')
_l_(1544806)
_c_(1544809, _a_(1544808, _n_(1544807, "plt", lambda: plt), "show"))
_l_(1544810)

z2 = _c_(1544822, _n_(1544811, "sinus2d", lambda: sinus2d), _c_(1544816, _a_(1544813, _n_(1544812, "np", lambda: np), "linspace"), 0,2*_a_(1544815, _n_(1544814, "np", lambda: np), "pi"),100)[:,None], _c_(1544821, _a_(1544818, _n_(1544817, "np", lambda: np), "linspace"), 0,2*_a_(1544820, _n_(1544819, "np", lambda: np), "pi"),100)[None,:])
_l_(1544823)

condition = _n_(1544824, "z", lambda: z)>0.6
_l_(1544825)
z_new = _n_(1544826, "z", lambda: z)[_n_(1544827, "condition", lambda: condition)] # This will make your array 1D
_l_(1544828) # This will make your array 1D

x_new = _n_(1544829, "xx", lambda: xx)[_n_(1544830, "condition", lambda: condition)]
_l_(1544831)
y_new = _n_(1544832, "yy", lambda: yy)[_n_(1544833, "condition", lambda: condition)]
_l_(1544834)
try:
    from scipy.interpolate import interp2d
    _l_(1544836)

except ImportError:
    pass
interpolated = _c_(1544841, _n_(1544837, "interp2d", lambda: interp2d), _n_(1544838, "x_new", lambda: x_new), _n_(1544839, "y_new", lambda: y_new), _n_(1544840, "z_new", lambda: z_new))
_l_(1544842)

interpolated_grid = _c_(1544850, _a_(1544847, _c_(1544846, _n_(1544843, "interpolated", lambda: interpolated), _n_(1544844, "xx", lambda: xx)[0], _n_(1544845, "yy", lambda: yy)[:, 0]), "reshape"), _a_(1544849, _n_(1544848, "xx", lambda: xx), "shape"))
_l_(1544851)

