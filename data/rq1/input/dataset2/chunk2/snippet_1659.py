#Source: https://stackoverflow.com/questions/55854898/typeerror-when-using-tf-keras-optimizers-apply-gradients-method-in-tensorflow-2
theta = tf.Variable(tf.zeros(100), dtype=tf.float32, name='theta')

@tf.function
def p(x):
    N = tf.cast(tf.shape(x)[0], tf.int64)
    softmax = tf.ones([N, 1]) * tf.math.softmax(theta)
    idx_x = tf.stack([tf.range(N, dtype=tf.int64), x-1], axis=1)
    return tf.gather_nd(softmax, idx_x)


@tf.function
def softmaxLoss(x):
    return tf.reduce_mean(-tf.math.log(p(x)))


train_dset = tf.data.Dataset.from_tensor_slices(data_train).\
                                repeat(1).batch(BATCH_SIZE)


# Create the metrics
loss_metric = tf.keras.metrics.Mean(name='train_loss')
val_loss_metric = tf.keras.metrics.Mean(name='val_loss')
optimizer = tf.keras.optimizers.Adam(0.001)

@tf.function
def train_step(inputs):
    with tf.GradientTape() as tape:
        log_loss = softmaxLoss(inputs)
    gradients = tape.gradient(log_loss,theta)
    optimizer.apply_gradients(zip(gradients, theta))
    # Update the metrics
    loss_metric.update_state(log_loss)


for epoch in range(NUM_EPOCHS):
    # Reset the metrics
    loss_metric.reset_states()

    # Shuffle dataset before each training epoch
    train_dset = train_dset.shuffle(buffer_size=10000)
    for inputs in train_dset:
        train_step(inputs)