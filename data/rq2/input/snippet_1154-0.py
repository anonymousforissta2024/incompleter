import numpy as np

def test_array_dimensions(ar1, ar2):
    try:
        ar1 + ar2
    except ValueError:
        return 'Different dimensions'
    else:
        return 'Same dimensions'
ar1 = np.arange(20).reshape(4, 5)
print(test_array_dimensions(ar1, ar2))
ar1 = np.arange(20).reshape(5, 4)
ar2 = np.arange(20).reshape(4, 5)
print(test_array_dimensions(ar1, ar2))