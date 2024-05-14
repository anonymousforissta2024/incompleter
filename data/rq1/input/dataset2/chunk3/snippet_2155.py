#Source: https://stackoverflow.com/questions/52749012/python-typeerror-1-is-not-a-string
import pandas as pd
import matplotlib.pylab as plt

data = pd.read_csv('sedimento.csv', encoding ='latin-1', delimiter=';', decimal=',')