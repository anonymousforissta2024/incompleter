#Source: https://stackoverflow.com/questions/75463626/typeerror-only-integer-tensors-of-a-single-element-can-be-converted-to-an-index
import numpy as np
import torch

theta = 0.6109
phi = 0.0
k0 = 6.2832
n_inc = 1.0

kinc = k0*n_inc*np.array([np.sin(theta)*np.cos(phi), 
                          np.sin(theta)*np.sin(phi), 
                          np.cos(theta)])
kinc = torch.tensor(kinc)
print(kinc)