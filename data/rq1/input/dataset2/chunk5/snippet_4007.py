#Source: https://stackoverflow.com/questions/41782239/typeerror-module-object-is-not-callable-selectivesearch
import skimage.data
import selectivesearch
import matplotlib.pyplot as plt
img = skimage.data.astronaut()
img_lbl, regions= selectivesearch.selectivesearch(img, scale=500, sigma=0.9, min_size=10)
regions[:10]
[{'labels': [0.0], 'rect': (0, 0, 15, 24), 'size': 260},
{'labels': [1.0], 'rect': (13, 0, 1, 12), 'size': 23}]