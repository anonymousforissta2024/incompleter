#Source: https://stackoverflow.com/questions/51126531/resizing-to-bigger-resolution-with-skimage-causes-shape-typeerror-in-keras
from  skimage import transform
new_shape = (48,88,3)
x_train = np.asarray([transform.resize(image, new_shape) for image in x_train])