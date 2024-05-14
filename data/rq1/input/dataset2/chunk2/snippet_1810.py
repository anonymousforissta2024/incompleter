#Source: https://stackoverflow.com/questions/59113341/typeerror-input-global-step-of-resourceapplyadagradda-op-has-type-int32-th
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import time

start_time = time.time()



data = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']

train_images = train_images/255.0

test_images = test_images/255.0

optimizer1 = tf.compat.v1.train.AdagradDAOptimizer(0.001,0)

model = keras.Sequential([
                           keras.layers.Flatten(input_shape=(28, 28)),
                           keras.layers.Dense(100, activation="softsign"),
                           keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer=optimizer1, loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(train_images, train_labels, epochs=5)

test_loss, test_acc1 = model.evaluate(test_images, test_labels)

print("Test acc is:", test_acc1)
print("--- %s seconds ---" % (time.time() - start_time))