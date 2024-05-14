#Source: https://stackoverflow.com/questions/63680459/typeerror-only-integers-slices-ellipsis-tf-newaxis-none-and
#load data from disk
X_patches=np.load("./x_training.npy").astype(np.float32)
Y_labels_valid=np.load("./y_training.npy").astype(np.float32)
X33_train=X_patches
Y_train=Y_labels
train_generator=img_msk_gen(X33_train=X_patches,Y_train=Y_labels,seed= 9999)
model.fit_generator(train_generator,steps_per_epoch=len(X33_train)//batch_size,
                    verbose=1)