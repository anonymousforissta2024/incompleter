#Source: https://stackoverflow.com/questions/72385774/how-solved-attributeerror-numpy-ndarray-object-has-no-attribute-lower
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk
from sklearn.feature_extraction.text import TfidfVectorizer

sting_array = ["hEllO","iNteRneT","pEopLe","sKay","sds","gbrhn","rHy"]
Array2D = np.reshape(sting_array, [-1, 1])
Lower = np.char.lower(Array2D)

stand = TfidfVectorizer()
 #fit data
Fit = stand.fit(Lower)
 #transform data
x_scaled =stand.transform(Lower)

print(x_scaled)