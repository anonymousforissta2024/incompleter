#Source: https://stackoverflow.com/questions/64780564/how-to-fix-attributeerror-module-tensorflow-has-no-attribute-session-in-han
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))