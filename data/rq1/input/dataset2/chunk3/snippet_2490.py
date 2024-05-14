#Source: https://stackoverflow.com/questions/61109095/typeerror-nonetype-object-is-not-subscriptable-when-i-train-a-cnn-model
kappa_metrics = Metrics()

history = model.fit(
    data_generator,
    steps_per_epoch = x_train.shape[0] / BATCH_SIZE,
    epochs = 15,
    validation_data = (x_val, y_val),
    callbacks = [kappa_metrics]
)