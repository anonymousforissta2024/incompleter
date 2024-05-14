# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-the-x-or-y-axis
# Note the super cluttered ticks on both X and Y axis.

# inputs
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = _c_(1545825, _a_(1545824, _n_(1545823, "np", lambda: np), "arange"), 1, 101)
_l_(1545826)
y = _n_(1545827, "x", lambda: x) * _c_(1545831, _a_(1545829, _n_(1545828, "np", lambda: np), "log"), _n_(1545830, "x", lambda: x)) 
_l_(1545832) 

fig = _c_(1545835, _a_(1545834, _n_(1545833, "plt", lambda: plt), "figure"))     # create figure
_l_(1545836)     # create figure
ax = _c_(1545839, _a_(1545838, _n_(1545837, "fig", lambda: fig), "add_subplot"), 111)
_l_(1545840)
_c_(1545845, _a_(1545842, _n_(1545841, "ax", lambda: ax), "plot"), _n_(1545843, "x", lambda: x), _n_(1545844, "y", lambda: y))
_l_(1545846)
_c_(1545850, _a_(1545848, _n_(1545847, "ax", lambda: ax), "set_xticks"), _n_(1545849, "x", lambda: x))        # set xtick values
_l_(1545851)        # set xtick values
_c_(1545855, _a_(1545853, _n_(1545852, "ax", lambda: ax), "set_yticks"), _n_(1545854, "y", lambda: y))        # set ytick values
_l_(1545856)        # set ytick values

_c_(1545859, _a_(1545858, _n_(1545857, "plt", lambda: plt), "show"))
_l_(1545860)

# inputs
x = _c_(1545863, _a_(1545862, _n_(1545861, "np", lambda: np), "arange"), 1, 101)
_l_(1545864)
y = _n_(1545865, "x", lambda: x) * _c_(1545869, _a_(1545867, _n_(1545866, "np", lambda: np), "log"), _n_(1545868, "x", lambda: x))
_l_(1545870)

fig = _c_(1545873, _a_(1545872, _n_(1545871, "plt", lambda: plt), "figure"))       # create figure
_l_(1545874)       # create figure
ax = _c_(1545877, _a_(1545876, _n_(1545875, "fig", lambda: fig), "add_subplot"), 111)
_l_(1545878)
_c_(1545883, _a_(1545880, _n_(1545879, "ax", lambda: ax), "plot"), _n_(1545881, "x", lambda: x), _n_(1545882, "y", lambda: y))
_l_(1545884)

_c_(1545888, _a_(1545886, _n_(1545885, "ax", lambda: ax), "set_xticks"), _n_(1545887, "x", lambda: x))
_l_(1545889)
_c_(1545893, _a_(1545891, _n_(1545890, "ax", lambda: ax), "set_yticks"), _n_(1545892, "y", lambda: y))
_l_(1545894)

# which values need to be shown?
# here, we show every third value from `x` and `y`
show_every = 3
_l_(1545895)

sparse_xticks = [None] * _a_(1545897, _n_(1545896, "x", lambda: x), "shape")[0]
_l_(1545898)
_n_(1545899, "sparse_xticks", lambda: sparse_xticks)[::_n_(1545900, "show_every", lambda: show_every)] = _n_(1545901, "x", lambda: x)[::_n_(1545902, "show_every", lambda: show_every)]
_l_(1545903)

sparse_yticks = [None] * _a_(1545905, _n_(1545904, "y", lambda: y), "shape")[0]
_l_(1545906)
_n_(1545907, "sparse_yticks", lambda: sparse_yticks)[::_n_(1545908, "show_every", lambda: show_every)] = _n_(1545909, "y", lambda: y)[::_n_(1545910, "show_every", lambda: show_every)]
_l_(1545911)

_c_(1545915, _a_(1545913, _n_(1545912, "ax", lambda: ax), "set_xticklabels"), _n_(1545914, "sparse_xticks", lambda: sparse_xticks), fontsize=6)   # set sparse xtick values
_l_(1545916)   # set sparse xtick values
_c_(1545920, _a_(1545918, _n_(1545917, "ax", lambda: ax), "set_yticklabels"), _n_(1545919, "sparse_yticks", lambda: sparse_yticks), fontsize=6)   # set sparse ytick values
_l_(1545921)   # set sparse ytick values

_c_(1545924, _a_(1545923, _n_(1545922, "plt", lambda: plt), "show"))
_l_(1545925)

