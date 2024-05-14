#Source: https://stackoverflow.com/questions/50913997/tensorflow-typeerror-tensorshape-object-is-not-callable
import tensorflow as tf
import numpy as np

tf.reset_default_graph()

input_x = tf.placeholder(name='tensor_a',shape=[None,None],dtype=tf.int32)
print(input_x.get_shape())

var_b = tf.get_variable('name_a',shape=[4,4],dtype=tf.float32,initializer=tf.random_uniform_initializer())
var_c = tf.get_variable('name_b',shape=[4,4],dtype=tf.float32,initializer=tf.random_uniform_initializer())
vac_d= tf.get_variable('name_d',shape=[var_c.shape[0],60],dtype=tf.float32,initializer=tf.random_uniform_initializer())
reshape_ = tf.reshape(var_c,[input_x.shape[0],input_x.shape[1],-1])
print(reshape_)
sum_c=tf.add(var_b,var_c)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(sum_c,feed_dict={input_x:np.random.randint(0,10,[2,2])}))