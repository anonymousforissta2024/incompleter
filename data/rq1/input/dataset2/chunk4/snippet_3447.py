#Source: https://stackoverflow.com/questions/69343020/cython-attribute-error-classes-vec-object-has-no-attribute-i
import pyximport; pyximport.install()
from Classes import line, Vec

L = line(Vec(0,0,4), Vec(5,6,6))