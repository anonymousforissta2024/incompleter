#Source: https://stackoverflow.com/questions/46650275/not-run-the-model-with-test-data-typeerror-cannot-interpret-feed-dict-key-as
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    iteration=0
    for e in range(epochs):
        for batch_x,batch_y in get_batch(train_x,train_y,batch_size):
            iteration+=1
            feed = {pred1.inputs: train_x,
                    pred1.y: train_y,
                    pred1.learning_rate: learning_rate_value,
                    pred1.is_training:True
                   }
            train_loss, _, train_acc = sess.run([pred1.cost, pred1.optimizer, pred1.accuracy], feed_dict=feed)
            if iteration % train_collect == 0:
                x_collect.append(e)
                train_loss_collect.append(train_loss)
                train_acc_collect.append(train_acc)
                if iteration % train_print==0:
                     print("Epoch: {}/{}".format(e + 1, epochs),
                      "Train Loss: {:.4f}".format(train_loss),
                      "Train Acc: {:.4f}".format(train_acc))       
                feed = {pred1.inputs: valid_x,
                        pred1.y: valid_y,
                        pred1.is_training:False
                       }
                val_loss, val_acc = sess.run([pred1.cost, pred1.accuracy], feed_dict=feed)
                valid_loss_collect.append(val_loss)
                valid_acc_collect.append(val_acc) 
                if iteration % train_print==0:
                    print("Epoch: {}/{}".format(e + 1, epochs),
                      "Validation Loss: {:.4f}".format(val_loss),
                      "Validation Acc: {:.4f}".format(val_acc))
    saver.save(sess, "./insurance2.ckpt")