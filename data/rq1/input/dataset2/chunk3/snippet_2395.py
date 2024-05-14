#Source: https://stackoverflow.com/questions/46795862/constrained-optimization-for-word2vec-giving-typeerror
optimizer = tf.contrib.opt.ScipyOptimizerInterface(loss, options={'max_iter': 5}, 
                                                    var_to_bounds = {self._emb: (-1., 1.), self._sm_w_t: (-1., 1.)},
                                                    method = 'SLSQP')
self._optimizer = optimizer