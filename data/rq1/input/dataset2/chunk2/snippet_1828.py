#Source: https://stackoverflow.com/questions/51126531/resizing-to-bigger-resolution-with-skimage-causes-shape-typeerror-in-keras
train_generator = datagen.flow(
    x_train, 
    batch_size=batch_size, 
    shuffle=True)