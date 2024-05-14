#Source: https://stackoverflow.com/questions/46650275/not-run-the-model-with-test-data-typeerror-cannot-interpret-feed-dict-key-as
model=multilayer_perceptron()
restorer=tf.train.Saver()
with tf.Session() as sess:
    restorer.restore(sess,"./insurance2.ckpt")
    feed={
        pred1.inputs:test_data,
        pred1.is_training:False
    }
    test_predict=sess.run(pred1.predicted,feed_dict=feed)