#Source: https://stackoverflow.com/questions/50625975/typeerror-ufunc-true-divide-output-typecode-d-could-not-be-coerced-to-pro
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import gower_function as gf

# Importing the dataset with pandas
dataset = pd.read_excel('input_partial.xlsx')
X = dataset.iloc[:, 1:].values
df = pd.DataFrame(X)
#obtaining gower distances of instances
Gower = gf.gower_distances(X)