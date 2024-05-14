#Source: https://stackoverflow.com/questions/59494717/typeerror-tensor-object-is-not-callable-keras-bert
inputs = model.inputs[:2] 
layer_output = model.get_layer('Encoder-12-FeedForward-Norm').output  
input_layer= keras.layers.Input(shape=(SEQ_LEN,768))(layer_output)
conv_layer= keras.layers.Conv1D(100, kernel_size=3, activation='relu', data_format='channels_first')(input_layer)   
maxpool_layer = keras.layers.MaxPooling1D(pool_size=4)(conv_layer)
flat_layer= keras.layers.Flatten()(maxpool_layer)
outputs = keras.layers.Dense(units=3, activation='softmax')(flat_layer)
model = keras.models.Model(inputs, outputs)
model.compile(RAdam(learning_rate =LR),loss='sparse_categorical_crossentropy',metrics=['sparse_categorical_accuracy'])