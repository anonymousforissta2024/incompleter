#Source: https://stackoverflow.com/questions/61173063/attributeerror-module-cupy-has-no-attribute-array
import numpy as np
import cupy as cp

x_gpu = cp.array([1, 2, 3])