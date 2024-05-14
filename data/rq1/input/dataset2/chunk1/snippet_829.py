#Source: https://stackoverflow.com/questions/38968649/failure-to-scale-in-pyclipper-typeerror-zero-object-is-not-iterable
from sympy.geometry.polygon import Polygon
import pyclipper as pc

start_list = [(0, 2), (2, 2), (2, 0), (0, 0)]
scaled = pc.scale_to_clipper(start_list)  # this works fine

as_poly = Polygon(*start_list)
new_list = [(pt.x, pt.y) for pt in as_poly.vertices]
assert new_list == start_list  # check that the lists are the same (this passes)

fail_to_scale = pc.scale_to_clipper(new_list)  # this fails