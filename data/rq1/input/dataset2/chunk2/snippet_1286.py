#Source: https://stackoverflow.com/questions/51277748/keras-attributeerror-tensor-object-has-no-attribute-log
def base_model():
   model = Sequential()
   model.add(Dense(50, input_dim=X_train.shape[1], init='normal',     activation='sigmoid'))
   model.add(Dropout(0.5))

   model.add(Dense(1, init='normal'))
   sgd = SGD(lr=0.01, momentum=0.8, decay=0.1, nesterov=False)
   model.compile(loss=rmsle, optimizer = sgd)# )'adam') #
   return model

keras = KerasRegressor(build_fn=base_model, nb_epoch=80, batch_size=1,verbose=1)
keras.fit(X_train ,y_train)