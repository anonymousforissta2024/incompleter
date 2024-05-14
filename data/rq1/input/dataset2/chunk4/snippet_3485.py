#Source: https://stackoverflow.com/questions/76352210/typeerror-variablemetaclass-variable-v1-call-got-an-unexpected-keyword-argum
encoder = [
    tf.keras.layers.InputLayer(input_shape=(32, 24, 1,)),
     tf.keras.layers.Conv2D(
        filters=32, kernel_size=3, strides=(2, 2), activation="gelu"
    )
]

tf.keras.Sequential(encoder).layers