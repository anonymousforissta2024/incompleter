#Source: https://stackoverflow.com/questions/51064323/tensorflow-typeerror-cannot-serialize-io-textiowrapper-object
x_ = [ tf.placeholder(tf.int32, shape=[None,], name='x{}'.format(i)) for i in range(xseq_len)]
y_ = [ tf.placeholder(tf.int32, shape=[None,], name='y{}'.format(i)) for i in range(yseq_len)]
decoder_inputs = [tf.zeros_like(x_[0], dtype=tf.int32, name = "GO")] + y_[:-1]
keep_prob = tf.placeholder(tf.float32)
basic_cell = tf.contrib.rnn.DropoutWrapper(tf.contrib.rnn.BasicLSTMCell(emb_dim),output_keep_prob=keep_prob)

stacked_lstm = tf.nn.rnn_cell.MultiRNNCell([basic_cell]*3)


with tf.variable_scope('decoder') as scope:
    decode_outputs, decode_states = seq2seq.embedding_rnn_seq2seq(x_,decoder_inputs, stacked_lstm,
                                        xvocab_size, yvocab_size, emb_dim)
    scope.reuse_variables()
#     # testing
    #decode_outputs_test, decode_states_test = #seq2seq.embedding_rnn_seq2seq(
        #x_, decoder_inputs, stacked_lstm, xvocab_size, #yvocab_size,emb_dim,
        #feed_previous=True)