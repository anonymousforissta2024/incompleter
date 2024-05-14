import numpy
px = (5, -2, 5)
qx, rx = numpy.polynomial.polynomial.polydiv(px, gx)
print(qx)
print(rx)