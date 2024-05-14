#Source: https://stackoverflow.com/questions/72521481/typeerror-can-only-concatenate-str-not-variablescope-to-str
sess = tf.compat.v1.Session()
sess, outMetrics = cft.train(sess, tf.compat.v1.train.AdamOptimizer, loss, metricsDict, trainingParam, feedDictFun, debug=True)