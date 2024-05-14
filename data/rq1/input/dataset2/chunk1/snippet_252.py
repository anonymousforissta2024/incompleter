#Source: https://stackoverflow.com/questions/47868014/zip-does-not-work-for-imshow-typeerror-image-data-cannot-be-converted-to-float
import matplotlib.pyplot as plt
a=[[1,2,3],[4,5,6]]
img_data=zip(*a)
plt.imshow(img_data)