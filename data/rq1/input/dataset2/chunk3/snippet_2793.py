#Source: https://stackoverflow.com/questions/53189543/adamoptimizer-returns-invalid-datatype-error
with tf.name_scope(name_scope):
    resh_inp = tf.reshape(input, [-1, 10, 10])
    input_shape = tf.shape(resh_inp)
    rows, cols = input_shape[1], input_shape[2]
    d_rows, d_cols = 2, 2
    subm_rows, subm_cols = rows - d_rows + 1, cols - d_cols + 1
    ii, jj = tf.meshgrid(tf.range(subm_rows), tf.range(subm_cols), indexing='ij')
    d_ii, d_jj = tf.meshgrid(tf.range(d_rows), tf.range(d_cols), indexing='ij')

    subm_ii = ii[:, :, tf.newaxis, tf.newaxis] + d_ii
    subm_jj = jj[:, :, tf.newaxis, tf.newaxis] + d_jj
    subm = tf.gather_nd(resh_inp[0, :, :], tf.stack([subm_ii, subm_jj], axis=-1), name=layer_name + "_gather")
    subm_sum = tf.reduce_sum(subm, axis=(2, 3), name=layer_name + "_subm_sum")
    _, top_idx = tf.nn.top_k(tf.reshape(subm_sum, [-1]), tf.minimum(k, tf.size(subm_sum)), name=layer_name + "_top_idx")
    top_row = top_idx // subm_cols
    top_col = top_idx % subm_cols
    result = tf.stack([top_row, top_col], axis=-1, name=layer_name + "_result")
    result_shape = tf.shape(result)
    result = tf.reshape(result, [-1, result_shape[0], result_shape[1]], name=layer_name + "_shaped_result")