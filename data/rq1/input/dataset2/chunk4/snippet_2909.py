#Source: https://stackoverflow.com/questions/66839062/typeerror-keyword-argument-not-understood-input-for-cnn-with-pretrained
def VGG16_MODEL(img_rows=IMG_SIZE, img_cols=IMG_SIZE, color_type=3):
    # Remove fully connected layer and replace
    # with softmax for classifying 10 classes
    model_vgg16_1 = VGG16(weights="imagenet", include_top=False)

    # Freeze all layers of the pre-trained model
    for layer in model_vgg16_1.layers:
        layer.trainable = False
        
    x = model_vgg16_1.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(CLASSES, activation = 'softmax')(x)

    model = Model(input = model_vgg16_1.input, output = predictions)
    
    return model

print("Model 1 network...")
model_vgg16_1 = VGG16_MODEL(img_rows=IMG_SIZE, img_cols=IMG_SIZE)

model_vgg16_1.summary()

model_vgg16_1.compile(loss='categorical_crossentropy',
                         optimizer='rmsprop',
                         metrics=['accuracy'])