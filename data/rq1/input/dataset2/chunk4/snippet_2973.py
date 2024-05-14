#Source: https://stackoverflow.com/questions/75619940/attributeerror-module-utils-has-no-attribute-svmtrain
import os
import numpy as np
import re

from matplotlib import pyplot
from scipy import optimize
from scipy.io import loadmat
import utils
import pandas as pd
from sklearn.metrics import accuracy_score

data = loadmat('ex6data1.mat')
X, y = data['X'], data['y'][:, 0]

utils.plotData(X, y)

pyplot.scatter(X[:,0], X[:,1], c=y)
pyplot.legend
pyplot.show()
C = 1
model = utils.svmTrain(X, y, C, utils.linearKernel, 1e-3, 20)
utils.visualizeBoundaryLinear(X, y, model)