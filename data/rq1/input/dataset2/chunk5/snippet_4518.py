#Source: https://stackoverflow.com/questions/52763000/numpy-code-works-in-repl-script-says-type-error
"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np
from math import e

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    results = []
    x = np.transpose(x)
    for j in range(len(x)):
        exps = [np.exp(s) for s in x[j]]
        _sum = np.sum(np.exp(x[j]))
        softmax = [i / _sum for i in exps]
        results.append(softmax)
    final = np.vstack(results)
    return np.transpose(final)
#    pass  # TODO: Compute and return softmax(x)


print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt 
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()