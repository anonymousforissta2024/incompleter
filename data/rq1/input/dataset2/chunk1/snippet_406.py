#Source: https://stackoverflow.com/questions/54011487/typeerror-unsupported-operand-types-for-image-and-int
from PIL import Image

image = Image.open(image_path)
image = np.array(image) / 255