#Source: https://stackoverflow.com/questions/58203138/typeerror-flow-from-directory-got-an-unexpected-keyword-argument-train-data
train_datagenerator = ImageDataGenerator(rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2)
train_generator = train_datagenerator.flow_from_directory(
    train_data_dir = '.\\Images\\data',
    target_size=(image_size, image_size), 
    batch_size=BATCH_SIZE_TRAINING,
    class_mode='categorical', subset='training') 
validation_generator = train_datagenerator.flow_from_directory(
    train_data_dir = '.\\Images\\data', 
    target_size=(image_size, image_size), 
    batch_size=BATCH_SIZE_TRAINING,
    class_mode='categorical', subset='validation')