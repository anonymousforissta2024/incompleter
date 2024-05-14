#Source: https://stackoverflow.com/questions/63492634/typeerror-init-missing-1-required-positional-argument-kernel-size
model = Sequential()
print(nb_filters[0], 'filters')
print('input shape', img_rows, 'rows', img_cols, 'cols', patch_size, 'patchsize')

model.add(Convolution3D(
    nb_filters[0],
    kernel_dim1=1, # depth
    kernel_dim2=nb_conv[0], # rows
    kernel_dim3=nb_conv[1], # cols
    input_shape=(1, img_rows, img_cols, patch_size),
    activation='relu'
))

model.add(MaxPooling3D(pool_size=(1, nb_pool[0], nb_pool[0])))

model.add(Dropout(0.2))

model.add(Flatten())

model.add(Dense(128, init='normal', activation='relu'))

model.add(Dropout(0.2))

model.add(Dense(nb_classes,init='normal'))

model.add(Activation('softmax'))
#optimizer adam,sgd,RMSprop,Adagrad,Adadelta,Nadam,
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])