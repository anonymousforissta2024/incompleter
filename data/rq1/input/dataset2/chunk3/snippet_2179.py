#Source: https://stackoverflow.com/questions/46650275/not-run-the-model-with-test-data-typeerror-cannot-interpret-feed-dict-key-as
def get_batch(data_x,data_y,batch_size=32):
    batch_n=len(data_x)//batch_size
    for i in range(batch_n):
        batch_x=data_x[i*batch_size:(i+1)*batch_size]
        batch_y=data_y[i*batch_size:(i+1)*batch_size]
        yield batch_x,batch_y

epochs = 25
train_collect = 20
train_print=train_collect*2

learning_rate_value = 0.001
batch_size=400

x_collect = []
train_loss_collect = []
train_acc_collect = []
valid_loss_collect = []
valid_acc_collect = []

saver = tf.train.Saver()