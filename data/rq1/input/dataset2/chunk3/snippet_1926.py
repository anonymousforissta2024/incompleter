#Source: https://stackoverflow.com/questions/58985632/attributeerror-module-tensorflow-core-keras-layers-has-no-attribute-conv1d
import tensorflow as tf
print(tf.__version__)

(mnist_train, minst_train_label), (mnist_test, mnist_test_label) = tf.keras.datasets.mnist.load_data()

train_label_batch_int = tf.cast(minst_train_label, tf.int32) ## This is important because one tf.one_hot does not accept float
train_label_batch_onehot = tf.one_hot(train_label_batch_int, depth = 10)
test_label_batch_int = tf.cast(mnist_test_label, tf.int32) ## This is important because one tf.one_hot does not accept float
test_label_batch_onehot = tf.one_hot(test_label_batch_int, depth = 10) 
## converting to ndarray
if type(train_label_batch_onehot).__name__ != 'ndarray' :
 train_label_batch_onehot = train_label_batch_onehot.numpy()
 test_label_batch_onehot = test_label_batch_onehot.numpy()

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers import Conv1D

model = tf.keras.Sequential([
tf.keras.layers.Conv1D(32,5,activation=tf.nn.relu),
tf.keras.layers.Conv1D(32,5,activation=tf.nn.relu),
tf.keras.layers.MaxPooling1D(2,2),

tf.keras.layers.Conv1d(64,3,activation=tf.nn.relu),
tf.keras.layers.MaxPooling1D(2,2),

tf.keras.layers.Conv1d(128,3,activation=tf.nn.relu),
tf.keras.layers.flatten(),
tf.keras.layers.Dense(1024,activation=tf.nn.relu),
tf.keras.layers.Dense(256,activation=tf.nn.relu),
tf.keras.layers.Dense(10,activation=None)])