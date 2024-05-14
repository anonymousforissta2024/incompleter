#Source: https://stackoverflow.com/questions/45209678/attributeerror-module-tensorflow-has-no-attribute-select
import tensorflow as tf
import numpy as np

A = 3
B = tf.convert_to_tensor([1, 2, 3, 4])
C = tf.convert_to_tensor([1, 1, 1, 1])
D = tf.convert_to_tensor([0, 0, 0, 0])

with tf.Session() as sess:
    print(sess.run(tf.select(A > 1, 'A', 'B')))
    print(sess.run(tf.select(False, 'A', 'B')))
    print(sess.run(tf.select(B > 2, C, D)))