#Source: https://stackoverflow.com/questions/59729859/python-typeerror-only-integer-scalar-arrays-can-be-converted-to-a-scalar-index
train_size = 3 # x_train.shape[0]
batch_size = 22
for i in range(242): # iters_num = 242
   batch_mask = np.random.choice(train_size, batch_size)
   print( t_train, batch_mask )
   x_batch = x_train[batch_mask]
   t_batch = t_label[batch_mask]