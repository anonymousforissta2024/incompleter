#Source: https://stackoverflow.com/questions/75964010/attributeerror-batchdataset-object-has-no-attribute-class-indices
img_height= 220
img_width= 220
batch_size= 64
train_ds= tf.keras.preprocessing.image_dataset_from_directory(
    train_path,
    validation_split= 0.2,
    subset='training',
    seed=123,
    image_size=(img_height,img_width),
    batch_size= batch_size
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    train_path,
    validation_split= 0.2,
    subset='validation',
    seed=123,
    image_size=(img_height,img_width),
    batch_size= batch_size,
    shuffle=False
)

test_ds = tf.keras.preprocessing.image_dataset_from_directory(
    test_path,
    seed=123,
    image_size=(img_height,img_width),
    batch_size= batch_size,
    shuffle=False
)