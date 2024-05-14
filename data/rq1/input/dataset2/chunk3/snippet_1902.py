#Source: https://stackoverflow.com/questions/52688788/typeerror-only-size-1-arrays-can-be-converted-to-python-scalars-when-trying-to
train_labels_GT = y_train[:,1] #Get Ground truth


print ('Writing train text file...')

data_dir = os.path.join(os.getcwd(), "Data/Out")


savetxt(os.path.join(data_dir, "train.txt"), x_train, True, y_train)
savetxt(os.path.join(data_dir, "test.txt"), x_test, True, y_test)


print("Done")