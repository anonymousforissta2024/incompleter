#Source: https://stackoverflow.com/questions/55314830/typeerror-not-supported-between-instances-of-nonetype-and-int
import pickle
import numpy as np
with open('rf_model_1','rb') as f:
    rf=pickle.load(f)

xx = np.array([67, 17832, 1, 1, 0, 33, 1941902452, 36, 33011.0, 19, 18, 0, 2, 1]).reshape(1,-1)
print('Class: ',int(rf.predict(xx)))