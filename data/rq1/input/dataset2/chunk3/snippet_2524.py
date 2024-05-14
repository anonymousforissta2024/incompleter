#Source: https://stackoverflow.com/questions/64282076/using-pretrained-model-with-keras-attributeerror-nonetype-object-has-no-attr
top_model_weight_path = 'feat_extr_model.h5'
train_data_dir = 'data/train'
validation_data_dir = 'data/validation'
nb_train_samples = 54
nb_validation_samples = 6
epochs = 10
batch_size = 16    

base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

top_model = Sequential()
top_model.add(Flatten(input_shape=base_model.output_shape[1:]))
top_model.add(Dense(256, activation='relu'))
top_model.add(Dropout(0.5))
top_model.add(Dense(1, activation='sigmoid'))
# note that it is necessary to start with a fully-trained
# classifier, including the top classifier,
# in order to successfully do fine-tuning
top_model.load_weights(top_model_weight_path)

model = Model(inputs=base_model.input, outputs=top_model(base_model.output))

for l in model.layers[:15]:
    l.trainable = False
model.compile(loss='binary_crossentropy',
              optimizer=optimizers.SGD(lr=1e-4, momentum=0.9),
              metrics=['accuracy'])

train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(train_data_dir,
                                                    target_size=(224, 224),
                                                    batch_size=batch_size,
                                                    class_mode=None)
validation_generator = test_datagen.flow_from_directory(validation_data_dir,
                                                        target_size=(224,224),
                                                        batch_size=batch_size,
                                                        class_mode=None)

model.summary()

# fine-tune the model
model.fit_generator(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator,
    verbose=2)