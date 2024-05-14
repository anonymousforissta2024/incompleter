#Source: https://stackoverflow.com/questions/70338776/typeerror-update-got-an-unexpected-keyword-argument-force
batch_size = 50
result = model.fit(
    X_train,
    Y_train,
    validation_data=(X_test, Y_test),
    batch_size=batch_size,
    epochs=5
)