#Source: https://stackoverflow.com/questions/75038713/how-to-solve-yellowbricktypeerror-the-supplied-model-is-not-a-clustering-estima
import matplotlib.pyplot as plt
from fcmeans import FCM
from yellowbrick.cluster import SilhouetteVisualizer

model = FCM(n_clusters=5, random_state=0)
visualizer = SilhouetteVisualizer(model, colors='yellowbrick')

visualizer.fit(X)        
visualizer.show()