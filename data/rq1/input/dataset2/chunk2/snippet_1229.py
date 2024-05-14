#Source: https://stackoverflow.com/questions/51711655/python-typeerror-init-got-an-unexpected-keyword-argument-serialized-opti
init = tf.global_variables_initializer()
sess = tf.Session()
writer = tf.summary.FileWriter("logs/",sess.graph) 
sess.run(init)