#Source: https://stackoverflow.com/questions/59338360/how-do-i-resolve-typeerror-not-supported-between-instances-of-int-and-st
class CustomModelCheckpoint(Callback):

    def __init__(self, model_parallel, path):

        super(CustomModelCheckpoint, self).__init__()

        self.save_model = model_parallel
        self.path = path
        self.nb_epoch = 0

    def on_epoch_end(self, epoch, logs=None):
        self.nb_epoch += 1
        self.save_model.save(self.path + str(self.nb_epoch) + '.hdf5')


i3d = i3d_modified(weights = 'rgb_imagenet_and_kinetics')
model = i3d.i3d_flattened(num_classes = num_classes)
optim = SGD(lr = 0.01, momentum = 0.9)

reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor = 0.1, patience = 10)
csvlogger = CSVLogger('i3d_'+model_name+'.csv')