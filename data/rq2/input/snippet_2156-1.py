import numpy as np
Input = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([7, 8, 9])]
for i in range(len(Input)):
    Output.append(np.mean(Input[i]))
print(Output)