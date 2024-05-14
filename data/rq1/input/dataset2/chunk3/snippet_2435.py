#Source: https://stackoverflow.com/questions/50913997/tensorflow-typeerror-tensorshape-object-is-not-callable
import tensorflow as tf
import numpy as np

tf.reset_default_graph()

input_x = tf.placeholder(name='tensor_a',shape=[2,3,4],dtype=tf.int32)

var_b = tf.get_variable('name_a',shape=[input_x.get_shape()[0],2],dtype=tf.float32,initializer=tf.random_uniform_initializer())
var_c = tf.get_variable('name_b',shape=[input_x.get_shape()[1],2],dtype=tf.float32,initializer=tf.random_uniform_initializer())

sum_c=tf.add(var_b,var_c)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(sum_c,feed_dict={input_x:np.random.randint(0,10,[2,3,4])}))