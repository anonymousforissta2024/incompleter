#Source: https://stackoverflow.com/questions/54232611/unexpected-type-error-using-numpy-save-and-savez
import numpy

test_path = "test.npy"
test_data = numpy.random.rand(100000)

with open(test_path, 'w') as test_file:
    numpy.save(test_file, test_data)