#Source: https://stackoverflow.com/questions/61036421/keras-shape-typeerror-tuple-object-is-not-callable
for data_batch, labels_batch in train_generator:
    print(data_batch.shape())