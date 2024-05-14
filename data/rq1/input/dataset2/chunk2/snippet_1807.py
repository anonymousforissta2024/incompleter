#Source: https://stackoverflow.com/questions/54064897/attributeerror-nonetype-object-has-no-attribute-image-data-format-in-keras
from keras import backend as K
from keras_applications.resnet50 import ResNet50
from keras.layers import Input
from keras.callbacks import ModelCheckpoint

K.set_image_data_format('channels_last')
K.set_image_dim_ordering('tf')

input_layer = Input(shape=(224, 224, 3))
model = ResNet50(include_top=True, weights=None, classes=2)
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])