#Source: https://stackoverflow.com/questions/44580123/typeerror-dot-operation-in-numpy-and-theano
import theano
import numpy

p=theano.tensor.dmatrix('p')
q=theano.tensor.dmatrix('q')
r=theano.tensor.dot(p,q)

f=theano.function([p,q], r)

a=numpy.array([1,2])
b=numpy.array([[1,2,3],[4,5,6]])