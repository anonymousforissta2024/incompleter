import numpy as np
print('Original matrix:\n')
print(X)
print('\nSubtract the mean of each row of the said matrix:\n')
Y = X - X.mean(axis=1, keepdims=True)
print(Y)