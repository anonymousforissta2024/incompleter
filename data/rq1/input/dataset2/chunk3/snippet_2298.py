#Source: https://stackoverflow.com/questions/60394722/why-does-it-say-this-typeerror-call-missing-1-required-positional-argum
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout
from keras.layers import Flatten, Activation
from keras.applications.vgg16 import VGG16
from keras.models import Model
from keras import backend as K

def swish(x):
    return K.sigmoid(x) * x

custom_vgg = Sequential()
img_width = 224
img_height = 224
vgg_model = VGG16(include_top=False, weights='imagenet',input_shape=(img_width, img_height, 3))
print(vgg_model.get_config())
#vgg_model.save_weights('models/vgg_weights.h5')
for layer in vgg_model.layers:
    if layer.__class__.__name__=='MaxPooling2D':
        layer.trainable = False
        custom_vgg.add(layer(activation = swish))
        custom_vgg.add(Dropout(0.4))
    else :
        custom_vgg.add(layer)
custom_vgg.add(Flatten())
custom_vgg.add(Dense(1024,activation=swish))
custom_vgg.add(Dense(1024,activation=swish))
custom_vgg.add(Dense(128, activation = "softmax"))

custom_vgg.compile(optimizer = "adam", loss = "categorical_crossentropy", metrics = ["accuracy"])

custom_vgg.summary() 