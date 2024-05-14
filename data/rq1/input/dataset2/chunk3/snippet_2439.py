#Source: https://stackoverflow.com/questions/46795862/constrained-optimization-for-word2vec-giving-typeerror
emb = tf.Variable(
    tf.random_uniform(
        [opts.vocab_size, opts.emb_dim], -init_width, init_width),
    name="emb")
self._emb = emb

sm_w_t = tf.Variable(
    tf.random_uniform(
        [opts.vocab_size, opts.emb_dim], -init_width, init_width),
    name="sm_w_t", dtype=tf.float32)
self._sm_w_t = sm_w_t