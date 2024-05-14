#Source: https://stackoverflow.com/questions/52114917/tensorflow-attributeerror-when-a-function-is-passed-to-another
input_X = tf.placeholder('float32', [None,64])
input_y = tf.placeholder('float32', [None,num_classes])

predicted_y = tf.sigmoid(tf.matmul(input_X, weights) + b)

def binary_logloss(true_y):

    if true_y ==1.:
        return tf.reduce_mean(tf.reduce_sum(-tf.log(predicted_y) , axis=1))
    elif true_y == 0.:
        return tf.reduce_mean(tf.reduce_sum(-tf.log(1-predicted_y) , axis=1))

def train_function(X, y):
    loss = binary_logloss(input_y)
    optimizer = tf.train.GradientDescentOptimizer(0.001).minimize(loss)
    _, c = s.run([optimizer, loss], {input_X:X, input_y:y})
    return _, c

s.run(tf.global_variables_initializer())
for epoch in epochs:     
    _, c = train_function(batch_x_train, batch_y_train) 