#Source: https://stackoverflow.com/questions/59541629/typeerror-input-y-of-mul-op-has-type-float32-that-does-not-match-type-int32
import numpy as np
import pandas as pd
import tensorflow as tf
w = tf.Variable(0, dtype=tf.float32)
cost = tf.add(tf.add(w**2, tf.multiply(-10,w)), 25)
train = tf.train.GradientDescentOptimizer(0.001).minimize(cost)

init = tf.global_variables_initializer()
session = tf.session()
session.run(init)
session.run(w)