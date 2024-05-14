#Source: https://stackoverflow.com/questions/53189543/adamoptimizer-returns-invalid-datatype-error
cost = tf.reduce_mean(tf.square(y_true - y_pred_cls))
optimizer = tf.train.AdamOptimizer(learning_rate=1e-4).minimize(cost)