#Source: https://stackoverflow.com/questions/57537474/how-to-fix-attributeerror-list-object-has-no-attribute-shape-error-in-pyt
from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from tensorflow import keras

print("Tensorflow Version:")
print(tf.version.VERSION)
print("Keras Verstion:")
print(tf.keras.__version__)

minst = tf.keras.datasets.mnist # 28x28 0-9

(x_train, y_train), (x_test, y_test) = minst.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x__test = x_test;
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1)

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)

model.save('epic_num.h5')
print("Saved")
# Loading

nmodel = keras.models.load_model("epic_num.h5")
import numpy as np;


# Test
predics = nmodel.predict([x_test])
print(predics)

import matplotlib.pyplot as plt

plt.imshow(x__test[11], cmap=plt.cm.binary)
plt.show()

print(np.argmax(predics[11]))