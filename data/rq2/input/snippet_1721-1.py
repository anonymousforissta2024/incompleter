import numpy
gx = (2, 1, 0)
qx, rx = numpy.polynomial.polynomial.polydiv(px, gx)
print(qx)
print(rx)