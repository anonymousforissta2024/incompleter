#Source: https://stackoverflow.com/questions/57526806/typeerror-fetch-argument-none-has-invalid-type-class-nonetype-at-tf-reduce
probab=tf.reduce_max(pred,  axis=1).eval()
sess.run(print(probab))