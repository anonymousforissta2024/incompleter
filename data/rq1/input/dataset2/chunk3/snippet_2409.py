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

    for batch in range(input_shape[0]):
        # x = tf.gather(x, batch)
        # print('tensor shape:', x.shape)  
        mask = np.empty(input_shape, dtype=np.float32)
        # for gamma
        mask.fill(1)
        mask[batch].fill(gamma[batch])
        x = Lambda(lambda tensor: tf.math.multiply(tensor, tf.convert_to_tensor(mask, dtype=tf.float32)))(input_img)
        print('multiply:', x.shape)
        # for beta
        mask.fill(1)
        mask[batch].fill(beta[batch])
        x = Lambda(lambda tensor: tf.math.add(tensor, tf.convert_to_tensor(mask, dtype=tf.float32)))(x)
        print('add:', x.shape)

    test = Model(inputs=input_img, outputs=x)
    return test

batch_sizes = [4, 8]
for i in batch_sizes:
    gamma = np.arange(i)
    beta = np.arange(i)
    model = build_test((i, 12, 12, 1))