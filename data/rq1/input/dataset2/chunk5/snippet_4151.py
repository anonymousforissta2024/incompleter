#Source: https://stackoverflow.com/questions/58168843/typeerror-init-missing-1-required-positional-argument-kernel-size
def fish_model():
    model = Sequential()
    from keras.layers import Activation, Dense
    from keras.layers.convolutional import Convolution2D
    from keras.layers.convolutional import MaxPooling2D
    from keras.layers import Dropout
    model.add(Convolution2D(filters=(6,3,3),input_shape=(256,768,1),activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2),strides=2))
    model.add(Convolution2D(filters=6, nb_row=3, nb_col=3,subsample=(2,2),
    input_shape=(256, 768, 1,), activation='relu', border_mode='same'))
    model.add(Dropout(0.1))
    model.add(Flatten())
    model.add(Dense(8, activation='softmax'))
    epochs = 5
    lrate = 0.1
    decay = lrate/epochs
    #sgd = SGD(lr=lrate, momentum=0.5, decay=decay, nesterov=False)
    model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['categorical_accuracy'])
    return model

model= fish_model()
print(model.summary())
history = model.fit(X_train, Y_train, validation_data=(x_validation, y_validation), nb_epoch=6, batch_size=4)