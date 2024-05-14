#Source: https://stackoverflow.com/questions/64236575/file-not-found-error-in-jupyter-lab-using-python
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns

df = pd.read_csv ('demo/big.csv')

print(df)