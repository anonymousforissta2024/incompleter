#Source: https://stackoverflow.com/questions/62785773/attributeerror-numpy-ndarray-object-has-no-attribute-assert-compile-was-cal
result = np.apply_along_axis(augment, axis=1, arr=X[C3]).reshape(-1, 187)
classe = np.ones(shape=(result.shape[0],), dtype=int)*3
X = np.vstack([X, result])
y = np.hstack([y, classe])
subC0 = np.random.choice(C0, 800)
subC1 = np.random.choice(C1, 800)
subC2 = np.random.choice(C2, 800)
subC3 = np.random.choice(C3, 800)
subC4 = np.random.choice(C4, 800)
X_test = np.vstack([X[subC0], X[subC1], X[subC2], X[subC3], X[subC4]])
y_test = np.hstack([y[subC0], y[subC1], y[subC2], y[subC3], y[subC4]])

X_train = np.delete(X, [subC0, subC1, subC2, subC3, subC4], axis=0)
y_train = np.delete(y, [subC0, subC1, subC2, subC3, subC4], axis=0)

X_train, y_train = shuffle(X_train, y_train, random_state=0)
X_test, y_test = shuffle(X_test, y_test, random_state=0)

del X
del y
X_train = np.expand_dims(X_train, 2)
X_test = np.expand_dims(X_test, 2)
history = tensorflow.keras.Model.fit(X_train, y_train, 
                epochs=75, 
                batch_size=batch_size, 
                verbose=2, 
                validation_data=(X_test, y_test), 
                callbacks= [lrate])