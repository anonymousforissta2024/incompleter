#Source: https://stackoverflow.com/questions/53189543/adamoptimizer-returns-invalid-datatype-error
x_p = tf.placeholder(tf.float32, shape=[None, img_size_flat*num_channels], name='x_pred')
x_pred_image = tf.reshape(x_p, [-1, 10, 10, num_channels])
k = tf.constant(npatches)
y_true = tf.placeholder(tf.int32, shape=[None, 2, 2], name='y_true')
y_true_cls = tf.placeholder(tf.int32, shape=[None, 2, 2], name='y_true_cls')