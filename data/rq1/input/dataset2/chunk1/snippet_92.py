#Source: https://stackoverflow.com/questions/51990034/simple-lstm-model-no-attr-named-xlacompile-in-name-error
model = Sequential()
model.add(Embedding(400001, emb_dim, trainable=False, input_length = 56, weights = [emb_matrix]))
model.add(LSTM(128, return_sequences=False))
model.add(Dense(5, activation='softmax'))
model.summary()
model.fit(train_in, train_out, epochs = 50, batch_size = 32, shuffle=True)