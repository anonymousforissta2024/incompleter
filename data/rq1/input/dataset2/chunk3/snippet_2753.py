#Source: https://stackoverflow.com/questions/61205314/nameerror-name-os-pathlike-is-not-defined
import numpy as np
import os

a = np.loadtxt(os.getcwd()+'abc.txt')