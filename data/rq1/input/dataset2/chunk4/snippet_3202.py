#Source: https://stackoverflow.com/questions/74611572/bayesianoptimization-search-errors-out-typeerror-float-object-is-not-subscri
tuner_nn.search(x_train, y_train, epochs=50, validation_data=(x_val,), verbose=0, callbacks=[Earlystopping])