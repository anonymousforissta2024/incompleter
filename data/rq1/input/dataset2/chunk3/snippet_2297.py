#Source: https://stackoverflow.com/questions/53272808/tensorflow-keras-typeerror-value-passed-to-parameter-labels-has-datatype-f
import tensorflow as tf
#tf.enable_eager_execution()
vocab_size=100
embedding_dim=256
seq_len=10
model=tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=seq_len))
model.add(tf.keras.layers.Dense(vocab_size))
model.compile(optimizer = tf.train.GradientDescentOptimizer(1.0),loss = tf.losses.sparse_softmax_cross_entropy)#tf.keras.metrics.sparse_categorical_crossentropy