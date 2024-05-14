#Source: https://stackoverflow.com/questions/42628141/attributeerror-module-tensorflow-has-no-attribute-streaming-accuracy
accuracy = tf.streaming_accuracy (y_pred,y_true,name='acc')
recall = tf.streaming_recall (y_pred,y_true,name='acc')
precision = tf.streaming_precision(y_pred,y_true,name='acc')
confusion = tf.confuson_matrix(Labels, y_pred,num_classes=10,dtype=tf.float32,name='conf')