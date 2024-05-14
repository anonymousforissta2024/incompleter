#Source: https://stackoverflow.com/questions/49338590/deep-neural-network-using-tensorflow-typeerror-variancescaling-object-is-not
n_input = 18
n_target = 1
n_hl1 = 10
n_hl2 = 10
n_hl3 = 10 

learning_rate = 0.1

batch_size = 100

X = tf.placeholder('float')
Y = tf.placeholder('float')

# Initializers
sigma = 1
weight_initializer = tf.variance_scaling_initializer(mode="fan_avg", distribution="uniform", scale=sigma)
bias_initializer = tf.zeros_initializer()

# Layer 1: Variables for hidden weights and biases
W_hidden_1 = tf.Variable(weight_initializer[n_input, n_hl1])
bias_hidden_1 = tf.Variable(bias_initializer([n_hl1]))

# Layer 2: Variables for hidden weights and biases
W_hidden_2 = tf.Variable(weight_initializer([n_hl1, n_hl2]))
bias_hidden_2 = tf.Variable(bias_initializer([n_hl2]))

# Layer 3: Variables for hidden weights and biases
W_hidden_3 = tf.Variable(weight_initializer([n_hl2, n_hl3]))
bias_hidden_3 = tf.Variable(bias_initializer([n_hl3]))

# Output layer: Variables for output weights and biases
W_out = tf.Variable(weight_initializer([n_hl3, n_target]))
bias_out = tf.Variable(bias_initializer([n_target]))

# Hidden layer
hidden_1 = tf.nn.relu(tf.add(tf.matmul(X, W_hidden_1), bias_hidden_1))
hidden_2 = tf.nn.relu(tf.add(tf.matmul(hidden_1, W_hidden_2), bias_hidden_2))
hidden_3 = tf.nn.relu(tf.add(tf.matmul(hidden_2, W_hidden_3), bias_hidden_3))

# Output layer (must be transposed)
out = tf.transpose(tf.add(tf.matmul(hidden_3, W_out), bias_out))


#prediction = neural_network_model(x)
cost =tf.reduce_mean(tf.squared_difference(out, Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)  

epochs = 1000

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for e in range(epochs):
        # Shuffle training data
        shuffle_indices = np.random.permutation(np.arange(len(y_data)))
        x_data = x_data[shuffle_indices]
        y_data = y_data[shuffle_indices]

        # Minibatch training
        for i in range(0, len(y_data) // batch_size):
            start = i * batch_size
            batch_x = x_data[start:start + batch_size]
            batch_y = y_data[start:start + batch_size]
            # Run optimizer with batch
            sess.run(optimizer, feed_dict={X: batch_x, Y: batch_y})  


    mse_final = sess.run(cost, feed_dict={X: x_test, Y: y_test})
    print(mse_final)