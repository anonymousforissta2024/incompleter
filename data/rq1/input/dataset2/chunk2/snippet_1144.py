#Source: https://stackoverflow.com/questions/41236090/attributeerror-module-tensorflow-python-summary-summary-has-no-attribute-sca
import tensorflow as tf
x = tf.Variable(tf.random_normal(5,5))
tf.summary.scalar('input', x)