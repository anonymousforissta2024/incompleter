#Source: https://stackoverflow.com/questions/34057159/attributeerror-function-object-has-no-attribute-quad-in-python
from scipy import linalg
from scipy.integrate import quad
import numpy as np


a = integrate.quad(lambda x: x**2, 0, 4.5)
print(a)