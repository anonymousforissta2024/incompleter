#Source: https://stackoverflow.com/questions/60870654/attributeerror-module-bezier-has-no-attribute-curve-error
import numpy as np
import bezier

nodes1 = np.asfortranarray([
[0.0, 0.5, 1.0],
[0.0, 1.0, 0.0]])

curve1 = bezier.Curve(nodes1, degree=2)