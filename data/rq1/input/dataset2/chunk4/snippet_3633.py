#Source: https://stackoverflow.com/questions/60019820/using-mnist-to-load-a-dataset-but-getting-file-not-found-error-windows-10-pyth
from mnist import MNIST
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
mndata = MNIST('.')
images, labels = mndata.load_training()