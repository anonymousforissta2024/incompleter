#Source: https://stackoverflow.com/questions/46650275/not-run-the-model-with-test-data-typeerror-cannot-interpret-feed-dict-key-as
from collections import namedtuple

def multilayer_perceptron():
    tf.reset_default_graph()
    inputs = tf.placeholder(tf.float32, shape=[None,train_x.shape[1]])
    y = tf.placeholder(tf.float32, shape=[None, 1])
    weights = {
    'h1': tf.Variable(tf.random_normal([train_x.shape[1], n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_hidden_2, 1]))
    }
    biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([1]))
    }
    # Hidden layer con funzione di attivazione ReLU
    layer_1 = tf.add(tf.matmul(inputs, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    # Hidden layer with ReLU activation
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)
    # Output layer with linear activation
    out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
    learning_rate = tf.placeholder(tf.float32)
    is_training=tf.Variable(True,dtype=tf.bool) 
    cross_entropy = tf.nn.sigmoid_cross_entropy_with_logits(labels=y,logits=out_layer )
    cost = tf.reduce_mean(cross_entropy)  
    with tf.control_dependencies(tf.get_collection(tf.GraphKeys.UPDATE_OPS)):
         optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
    predicted = tf.nn.sigmoid(out_layer) 
    correct_pred = tf.equal(tf.round(predicted), y)
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
    # Export the nodes 
    export_nodes = ['inputs', 'y', 'learning_rate','is_training', 'out_layer',
                    'cost', 'optimizer', 'predicted',  'accuracy'] 
    Graph = namedtuple('Graph', export_nodes)
    local_dict = locals()
    graph = Graph(*[local_dict[each] for each in export_nodes])
    return graph

pred1 = multilayer_perceptron()