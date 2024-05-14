#Source: https://stackoverflow.com/questions/44946189/typeerror-init-got-an-unexpected-keyword-argument-shape
import tensorflow as tf

g1 = tf.Graph()
with g1.as_default():
    v = tf.get_variable("v", initializer=tf.zeros_initializer(shape=[1]))