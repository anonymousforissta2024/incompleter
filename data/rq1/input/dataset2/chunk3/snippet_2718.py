#Source: https://stackoverflow.com/questions/58226787/nonetype-error-in-lambda-layer-while-applying-a-mask-to-a-tensor
import tensorflow as tf
from tensorflow.keras.layers import Conv2D, Input, BatchNormalization
from tensorflow.keras.layers import Lambda, Multiply, Add, Reshape
from tensorflow.keras.models import Model
import tensorflow.keras.backend as K
import numpy as np

def build_test(input_shape):
    input_img = Input(shape=input_shape)
    print('Input reshape:', input_shape)

    x = Lambda(lambda tensor, mask: tf.math.multiply(tensor, tf.convert_to_tensor(mask, dtype=tf.float32)))([input_img, gamma])
    print('multiply:', x.shape)
    x = Lambda(lambda tensor, mask: tf.math.add(tensor, tf.convert_to_tensor(mask, dtype=tf.float32)))([x, beta])
    print('add:', x.shape)

    test = Model(inputs=input_img, outputs=x)
    return test

batch_sizes = [4, 8]
for i in batch_sizes:
    gamma = np.arange(i)
    beta = np.arange(i)
    model = build_test((i, 12, 12, 1))