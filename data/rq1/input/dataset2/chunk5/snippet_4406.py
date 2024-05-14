#Source: https://stackoverflow.com/questions/43809513/getting-attributeerror-module-matplotlib-image-has-no-attribute-frombyte-i
import matplotlib.pyplot as plt
image = caffe.io.load_image(root + 'images/cat.jpg')
transformed_image = transformer.preprocess('data', image)
plt.imshow(image)