#Source: https://stackoverflow.com/questions/61036421/keras-shape-typeerror-tuple-object-is-not-callable
train_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2) # set validation split

train_generator = train_datagen.flow_from_directory(
    directory=r"path_to_the_train_dir",
    target_size=(128, 128),
    class_mode="binary",
    shuffle=True,
    seed=42,
    subset='training' # set as training data
)

validation_generator = train_datagen.flow_from_directory(
    directory=r"path_to_the_train_dir", # same directory as training data
    target_size=(128, 128),
    class_mode='binary',
    subset='validation') # set as validation data