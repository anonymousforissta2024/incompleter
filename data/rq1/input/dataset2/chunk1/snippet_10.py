#Source: https://stackoverflow.com/questions/57224598/attributeerror-module-matlab-has-no-attribute-engine
import matlab
from numpy import *
import sys
if __name__ == '__main__':
    print(sys.maxsize > 2 ** 32)
    eng = matlab.engine.connect_matlab()
    names = matlab.engine.find_matlab()
    print(names)

    eng = matlab.engine.start_matlab()
    A = matlab.double([[1,2],[5,6]])
    print(type(A),A.size,A)
    print(eng.eig(A))
    eng.quit()
    pass